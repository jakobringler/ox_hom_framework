from ox.base_objects.ox_node import OXNode
from ox.base_objects.parameter import Parameter
from ox.base_objects.menu import Menu
# node class version: 0.1


class SphereNode(OXNode):
    node_type = 'sphere'
    parm_lookup_dict = {'type': 'type', 'surftype': 'surftype', 'radx': 'radx', 'rady': 'rady', 'radz': 'radz', 'tx': 'tx', 'ty': 'ty', 'tz': 'tz', 'rx': 'rx', 'ry': 'ry', 'rz': 'rz', 'scale': 'scale', 'orient': 'orient', 'freq': 'freq', 'rows': 'rows', 'cols': 'cols', 'orderu': 'orderu', 'orderv': 'orderv', 'imperfect': 'imperfect', 'upole': 'upole', 'accurate': 'accurate', 'triangularpoles': 'triangularpoles'}

    def __init__(self, node=None, ox_parent=None, node_name=None):
        self.ox_parent = ox_parent
        if node:
            self.node = node
        else:
            self.node = self.ox_parent.create_node(node_type_name=self.node_type, node_name=node_name)
        self.node_name = self.node.name()
        super().__init__(node=self.node)
        
        # parm vars:
        self.parm_radx = Parameter(parm=self.node.parm('radx'))
        self.parm_rady = Parameter(parm=self.node.parm('rady'))
        self.parm_radz = Parameter(parm=self.node.parm('radz'))
        self.parm_tx = Parameter(parm=self.node.parm('tx'))
        self.parm_ty = Parameter(parm=self.node.parm('ty'))
        self.parm_tz = Parameter(parm=self.node.parm('tz'))
        self.parm_rx = Parameter(parm=self.node.parm('rx'))
        self.parm_ry = Parameter(parm=self.node.parm('ry'))
        self.parm_rz = Parameter(parm=self.node.parm('rz'))
        self.parm_scale = Parameter(parm=self.node.parm('scale'))
        self.parm_freq = Parameter(parm=self.node.parm('freq'))
        self.parm_rows = Parameter(parm=self.node.parm('rows'))
        self.parm_cols = Parameter(parm=self.node.parm('cols'))
        self.parm_orderu = Parameter(parm=self.node.parm('orderu'))
        self.parm_orderv = Parameter(parm=self.node.parm('orderv'))
        self.parm_imperfect = Parameter(parm=self.node.parm('imperfect'))
        self.parm_upole = Parameter(parm=self.node.parm('upole'))
        self.parm_accurate = Parameter(parm=self.node.parm('accurate'))
        self.parm_triangularpoles = Parameter(parm=self.node.parm('triangularpoles'))

        
        # parm menu vars:
        self.parm_type = TypeMenu(parm=self.node.parm('type'))
        self.parm_surftype = SurftypeMenu(parm=self.node.parm('surftype'))
        self.parm_orient = OrientMenu(parm=self.node.parm('orient'))


        # input vars:
        self.input_bounding_source = 'Bounding Source'


# parm menu classes:
class TypeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_primitive = "prim"
        self.menu_polygon = "poly"
        self.menu_polygon_mesh = "polymesh"
        self.menu_mesh = "mesh"
        self.menu_nurbs = "nurbs"
        self.menu_bezier = "bezier"
        self.menu_polygon_soup = "polysoup"


class SurftypeMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_rows = "rows"
        self.menu_columns = "cols"
        self.menu_rows_and_columns = "rowcol"
        self.menu_triangles = "triangles"
        self.menu_quadrilaterals = "quads"
        self.menu_alternating_triangles = "alttriangles"
        self.menu_reverse_triangles = "revtriangles"


class OrientMenu(Menu):
    def __init__(self, parm):
        self.parm = parm
        super().__init__(parm=parm)
        self.menu_x_axis = "x"
        self.menu_y_axis = "y"
        self.menu_z_axis = "z"



