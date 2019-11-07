import SimpleITK as sitk
import read_image_m as RIM
import os
import itk
def read(read_string):
    ext=os.path.splitext(read_string)[1]
    m_string=read_string
    if (ext==".nii" or ext==".nrrd"):

        Inner_volume=sitk.ReadImage(m_string)
    else:
        Inner_volume=RIM.dicom_series_reader(m_string)

    return Inner_volume
