import vtk
#directory of the ply function that you want to read
filename = "writeply.ply"
#directory for writing  stl file
write_string="write_stl.stl"

###############In case you do not have ply file you can create an sphere and write it as PLY
# sphereSource = vtk.vtkSphereSource()
# sphereSource.Update()
#
# plyWriter = vtk.vtkPLYWriter()
# plyWriter.SetFileName(filename)
# plyWriter.SetInputConnection(sphereSource.GetOutputPort())
# plyWriter.Write()

#Read and display for verication
reader = vtk.vtkPLYReader()
reader.SetFileName(filename)
reader.Update()

stlWriter = vtk.vtkSTLWriter()
stlWriter.SetFileName(write_string)
stlWriter.SetInputData(reader.GetOutput())
stlWriter.Write()
mapper = vtk.vtkPolyDataMapper()
mapper.SetInputConnection(reader.GetOutputPort())

actor = vtk.vtkActor()
actor.SetMapper(mapper)

renderer = vtk.vtkRenderer()
renderWindow = vtk.vtkRenderWindow()
renderWindow.AddRenderer(renderer)
renderWindowInteractor = vtk.vtkRenderWindowInteractor()
renderWindowInteractor.SetRenderWindow(renderWindow)

renderer.AddActor(actor)
renderer.SetBackground(.3, .6, .3)   #Background color green

renderWindow.Render()
renderWindowInteractor.Start()
