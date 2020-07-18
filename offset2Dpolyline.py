import cadquery as cq

points = [ (1.0, 0.0), (0.3, 0.2), (0.0, 0.0), (0.3, -0.1), (1.0, -0.03)]

outside = (
    cq.Workplane("front")
    .polyline(points).close()
    .extrude(1)
)
#show_object(outside)

# IndexError if thickness >= -0.15
thickness=-0.01
inside = (
    cq.Workplane("front")
    .polyline(points).close()
    .offset2D(thickness, 'intersection')
    .extrude(1)
)
#show_object(inside)

result = outside.cut(inside)
show_object(result)
