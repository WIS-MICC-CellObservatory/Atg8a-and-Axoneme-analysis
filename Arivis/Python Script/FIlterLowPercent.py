import math
import time
import arivis
import arivis_operation, arivis_core, arivis_objects, arivis_parameter
import numpy as np

"""
Get as input objects of verious volumes and sums up all the volumes and remove the smallest 20%
"""

@arivis_parameter.add_arivis_parameters(input_tag = "[ENTER_OBJECT_TAG_HERE]", cut_off = 20) #, channel = 1, custom_feature1 = "Intensities LOG10", custom_feature2= "Density %")
#arivis_parameter.add_param_description(input_tag = "Objects with specified tag are processed.", channel = "Index of channel of interest. First channel has index 1.")
def main(input_tag, cut_off):#, channel, custom_feature1, custom_feature2):
  startTime = time.time()

  # get inputs (and it's info) and output
  context = arivis_operation.Operation.get_context()
  input_object_data = context.get_input(0)
  #input_voxel_data = context.get_input(1)
  output_data = context.get_output()

  #pixelType = input_voxel_data.get_pixel_type()

  #custom_log_feature_name = custom_feature1 + "#" + str(channel)
  #custom_perecntage_feature_name = custom_feature2
  #create_cutom_features(output_data, [custom_log_feature_name, custom_perecntage_feature_name])

  #if pixelType == ('H' or 'I' or 'L' or 'f'):
  #  coefficent = int(65535)   
  #else:     
  #  coefficent = int(255)

  # get the id of objects with the given input tag
  obj_ids = input_object_data.get_object_ids(input_tag)
  if obj_ids.__len__() == 0 :
    print( "No object with specified tag exist. End of script!" )
  
  else:
    totalWork = obj_ids.__len__()
    workDone = 0
    
    object_volumes = np.zeros(totalWork,dtype=float)
    for i in range(totalWork):
    #for id in obj_ids:
    
      object = input_object_data.get_object(obj_ids[i], True)
      #object_sum_intensity, volume_voxels = get_object_intensity_volume(object, channel, input_object_data)
      object_volumes[i] = get_object_volume(object, input_object_data)
      #object_intensity_log = math.log10(object_sum_intensity)

      #volume_voxels *= coefficent
      #object_intensity_percentage = 0.0
      #if volume_voxels > 0.0: 
      #    object_intensity_percentage = (object_sum_intensity / volume_voxels) * 100.0
      
      #print("id:",id,"volume",object_volume)
      #if object_volume > 1:
      #output_data.add_object(object)
      #set_object_custom_featue_Values(object, output_data, custom_log_feature_name, object_intensity_log, custom_perecntage_feature_name, object_intensity_percentage)

      workDone = workDone + 1
      context.notify_progress(workDone * 100 / totalWork*2)
        
    object_sum_volumes = np.sort(object_volumes)
    for i in range(totalWork-1):
      object_sum_volumes[i+1] += object_sum_volumes[i]
      
    threshold = object_sum_volumes[totalWork-1]
    for i in range(1,totalWork):
      if object_sum_volumes[i]/object_sum_volumes[totalWork-1] > cut_off/100:
        threshold = object_sum_volumes[i]-object_sum_volumes[i-1]
        break
    for i in range(totalWork):
      if object_volumes[i] >= threshold:
        object = input_object_data.get_object(obj_ids[i], True)
        output_data.add_object(object)
        
      workDone = workDone + 1
      context.notify_progress(workDone * 100 / totalWork*2)
      
  endTime = time.time()
  print ("time: " + str(endTime - startTime))


############################################## helper methods #############################################################

def create_cutom_features(output_data, features_names):
  """
  creates new custom features, these features are listed in object dialog -> feature list
  """
  for feat_name in features_names:
    custom_feature = arivis_objects.FeatureDescriptor()
    custom_feature.set_name(feat_name)
    custom_feature.set_id(feat_name)

    custom_feat_desc = arivis_objects.ValueDescriptor()
    custom_feat_desc.set_type(arivis_objects.ValueDescriptor.TYPE_FLOAT)
    custom_feat_desc.set_name(feat_name)
    custom_feat_desc.set_unit("GL") 
    
    custom_feature.add_value(custom_feat_desc)
    success = output_data.create_stored_feature(custom_feature)

    if success == False:
      print ("Could not create a new feature for " + feat_name + ". It already exists.")


def get_object_intensity_volume(object, channel, input_object_data):
  """
  gets the sum intensity and volume (voxels) of the given object over specified channel
  """
  feature_desc = input_object_data.get_feature_descriptor("Intensities #" + str(channel)) 
  if feature_desc is None:
    raise ValueError("There is no feature descriptor for feature_name: Intensities # for channel: " , channel)

  intensities = input_object_data.get_feature_for_object(feature_desc,object) 
  feature_values = intensities.get_values()
  sum_intensity = 1.0 if feature_values[3] <= 0 else feature_values[3]
  print("sum intensity for object with id " , str(object.get_id()), " over channel " , str(channel) + " is: " , str(sum_intensity))
  
  feature_desc = input_object_data.get_feature_descriptor("Volume")   
  if feature_desc is None:
    raise ValueError("There is no feature descriptor for feature_name : Volume")

  volume = input_object_data.get_feature_for_object(feature_desc,object)
  feature_values = volume.get_values() 
  volume_micron = feature_values[0]
  volume_voxels = feature_values[1]
  print("volume (voxel count) for object with id "+ str(object.get_id()) + " is: " + str(volume_voxels))

  return sum_intensity, volume_voxels
   
def get_object_volume(object, input_object_data):
  """
  gets volume (micron) of the given object over specified channel
  """
  feature_desc = input_object_data.get_feature_descriptor("Volume")   
  if feature_desc is None:
    raise ValueError("There is no feature descriptor for feature_name : Volume")

  volume = input_object_data.get_feature_for_object(feature_desc,object)
  feature_values = volume.get_values() 
  volume_micron = feature_values[0]
  volume_voxels = feature_values[1]
  #print("volume (voxel count) for object with id "+ str(object.get_id()) + " is: " + str(volume_voxels))

  return volume_micron

def set_object_custom_featue_Values(object, output_data, feature1_name, feature1_value, feature2_name, feature2_value):
  """
  sets the custom feature values for the given object 
  """
  feature_desc = output_data.get_feature_descriptor(feature1_name)
  if None == feature_desc:
    print (feature1_name + " does not exist")
    return 
 
  feature = arivis_objects.Feature()
  feature.set_value(feature1_name,feature1_value)
  output_data.set_feature_for_object(feature,feature_desc,object)

  feature_desc = output_data.get_feature_descriptor(feature2_name)
  if None == feature_desc:
    print (feature2_name + " does not exist")
    return 
 
  feature = arivis_objects.Feature()
  feature.set_value(feature2_name,feature2_value)
  output_data.set_feature_for_object(feature,feature_desc,object)


