import cadquery as cq

points = [ (1.0, 0.0), (0.3, 0.2), (0.0, 0.0), (0.3, -0.1), (1.0, -0.03)]

# ValueError if thickness >= -0.0184
thickness=-0.01
result = (
    cq.Workplane("front")
    .polyline(points).close()
    .extrude(1)
    .shell(thickness)
)
show_object(result)
