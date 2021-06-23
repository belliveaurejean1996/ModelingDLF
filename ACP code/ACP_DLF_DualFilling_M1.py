# this is a code that will generate a random orientation and position for a DLF chip based on a uniform random pattern

# Import package needed
import numpy as np
from numpy.core.shape_base import hstack, stack
from numpy.lib.function_base import angle

# --------------------------- Parameters --------------------------------------------------

# CHIP DIMENTION (M)
CDIMX = 12.5e-3  # length of the chips
CDIMY = 12.5e-3  # heigth of the chips
CDIMZ = 0.14e-3  # thickness of each chip

# GEOMERTY PARAMETER
LENGTH = 150e-3  # LENGTH OF THE SPECIMEN (X DIRECTION)
HEIGTH = 25e-3  # HEIGTH OF THE SPECIMEN (Y DIRECTION)
PLY = 18  # NUMBER OF CHIPS IN THE Z DIRECTION
THICK = PLY * CDIMZ  # HEIGTH OF THE SPECIMEN (Z DIRECTION)

# ----------------------------- Generate the mesh grid ---------------------------------------

# MESHGRID PARAMERTERS
NELMX = 150  # NUMBER OF ELEMENTS IN THE Y DIRECTION
NELMY = 25  # NUMBER OF ELEMENTS IN THE X DIRECTION

# Import the position of the elements
X = np.linspace(0,LENGTH,NELMX)
Y = np.linspace(0,HEIGTH,NELMY)
Xposition, Yposition = np.meshgrid(X, Y)
Q = len(X)*len(Y)
Xpos = np.reshape(Xposition,Q)
Ypos = np.reshape(Yposition,Q)

# ------------------------ Main Functions -----------------------------------------------------------

# Function that generates a random position and orientation for the chip
def ChipOrientation(sl, sh):
    x = np.random.rand(1) * sl # Randome position in X
    y = np.random.rand(1) * sh # Randome position in y

    #angle = (np.random.rand(1) * 180) - 90 # Randome angle of the chip
    mu, sigma = 90, 45 # mean and standard deviation
    angle = np.random.normal(mu, sigma, 1)
    if angle > 90:
        angle = angle - 180

    return angle, x, y

# Function that checks what elements are inside of that chip based on element position
def ElementPosition(chipprop, xpos, ypos, ChipX, ChipY):

    # surface area of the chip
    area = ChipX * ChipY

    # Chip Random position and orientation
    angle = chipprop[0]
    x = chipprop[1]
    y = chipprop[2]

    # position of each corner of the chip
    # top left
    x1 = x[0] - ((ChipX / 2) * np.cos(np.deg2rad(angle))) - ((ChipY / 2) * np.sin(np.deg2rad(angle)))
    y1 = y[0] - ((ChipX / 2) * np.sin(np.deg2rad(angle))) + ((ChipY / 2) * np.cos(np.deg2rad(angle)))
    # top right
    x2 = x[0] + ((ChipX / 2) * np.cos(np.deg2rad(angle))) - ((ChipY / 2) * np.sin(np.deg2rad(angle)))
    y2 = y[0] + ((ChipX / 2) * np.sin(np.deg2rad(angle))) + ((ChipY / 2) * np.cos(np.deg2rad(angle)))
    # bottom right
    x3 = x[0] + ((ChipX / 2) * np.cos(np.deg2rad(angle))) + ((ChipY / 2) * np.sin(np.deg2rad(angle)))
    y3 = y[0] + ((ChipX / 2) * np.sin(np.deg2rad(angle))) - ((ChipY / 2) * np.cos(np.deg2rad(angle)))
    # bottom left
    x4 = x[0] - ((ChipX / 2) * np.cos(np.deg2rad(angle))) + ((ChipY / 2) * np.sin(np.deg2rad(angle)))
    y4 = y[0] - ((ChipX / 2) * np.sin(np.deg2rad(angle))) - ((ChipY / 2) * np.cos(np.deg2rad(angle)))

    # calculate what elements air inside to chips
    ABP = np.abs(((x1 * y2) + (x2 * ypos) + (xpos * y1) - (y1 * x2) - (y2 * xpos) - (ypos * x1)) / 2)
    ADP = np.abs(((x1 * y3) + (x3 * ypos) + (xpos * y1) - (y1 * x3) - (y3 * xpos) - (ypos * x1)) / 2)
    DCP = np.abs(((x3 * y4) + (x4 * ypos) + (xpos * y3) - (y3 * x4) - (y4 * xpos) - (ypos * x3)) / 2)
    BCP = np.abs(((x4 * y2) + (x2 * ypos) + (xpos * y4) - (y4 * x2) - (y2 * xpos) - (ypos * x4)) / 2)
    add = ABP + ADP + DCP + BCP

    # determine if element is inside of the chip
    index = np.where(add <= area, True, False)
    ELM = np.where(index == 1)
    ELEMENT = ELM[0]
    return ELEMENT # Output the element index which are inside of the chip location


# function that will create the stack up squence for a 
def Stackup(PLY, Q, Xpos, Ypos, CDIMX, CDIMY, LENGTH, HEIGTH):

    # Create array of Z position (initialy the matrix is set to all zeros to fill up the first row)
    Zpos = np.zeros(len(Xpos))

    # Array for the stack up squence and check if all element are filled
    Filled = np.full((Q, PLY+1), False)
    Orientation = np.zeros((Q, PLY+1))

    i = 0
    check = False
    while check < 1:

        ChipProp = ChipOrientation(LENGTH, HEIGTH) # generate the randome position and orientation of the chip [angle, X, Y]
        Ind = ElementPosition(ChipProp, Xpos, Ypos, CDIMX, CDIMY) # Find the index of all the elements inside of the chip [all the element index]

        # Insert the chip angles in the Orientation Matrix based on the element index matrix Ind
        for j in range(len(Ind)):

            # Change the position of Z to have an over lap of chips
            Zpos[Ind[j]] += 1

            # Place the Angle of the element in the Orientation Array
            if Zpos[Ind[j]] < PLY+1:
                row = Ind[j]
                col = int(Zpos[Ind[j]])
                Orientation[row, col] = ChipProp[0]
                Filled[row, col] = True

        # Check if all the elements are filled
        Arr = np.amin(Filled, axis=0)
        Arr = Arr[1:19]
        check = np.all(Arr, axis=0)

        # juste la pour pas que sa va a l'infinit
        i += 1
        if i == 100000:
            check = True
            print('not enough chips')

    Orientation = Orientation[:,1:PLY+1]

    return Orientation

# ------------------ create the chips positions -------------------------------

# Chip orientation
stackup1 = Stackup(int(PLY/2), Q, Xpos, Ypos, CDIMX, CDIMY, LENGTH, HEIGTH)
stackup2 = Stackup(int(PLY/2), Q, Xpos, Ypos, CDIMX, CDIMY, LENGTH, HEIGTH)
stackup = np.hstack((stackup1, np.flip(stackup2, 1)))

# Chip position
Zloc = np.zeros(len(Xpos))
Location = np.vstack((Xpos,Ypos,Zloc))

# -------------------------------- export the data ------------------------------
LookUpData = np.hstack((Location.T,stackup))
np.savetxt(r'E:\Universite\Matrise\Article - Comparison\WorkbenchWorking\ACP code\LookUpData.csv', LookUpData, delimiter=",")

# -------------------------------- ACP model ------------------------------------

# Create a model variable
myModel = db.models['ACP Model']

# set the unit systeme
myModel.unit_system = 'mks'

# create the fabric material
myFabric = myModel.material_data.create_fabric( name='Fabric.1')
myFabric.thickness = CDIMZ
myFabric.material = myModel.material_data.materials['UDchips']

# define element set
myElements = myModel.element_sets['All_Elements']

# create the global rosette
myRossette = myModel.create_rosette( name='Rosette.1', show=True )
myRossette.origin = (LENGTH/2, HEIGTH/2, 0.0)

# create a lookup table (loop)
myTable = myModel.create_lookup_table3d(name='LookUpTable3D.1')
myTable.columns['Location'].values = Location.T

for i in range(stackup.shape[1]):
    myTable.create_column( name='Ply'+str(i), type='scalar' )
    myTable.columns['Ply'+str(i)].values = stackup[:,i]

# create the orientation selection set for all the elements
myModel.create_oriented_selection_set(name='OrientedSelectionSet.1')
myModel.oriented_selection_sets['OrientedSelectionSet.1'].element_sets=[myElements]
myModel.oriented_selection_sets['OrientedSelectionSet.1'].rosettes=[myRossette]
myModel.oriented_selection_sets['OrientedSelectionSet.1'].orientation_direction = (0.0, 0.0, 1.0)
myModel.oriented_selection_sets['OrientedSelectionSet.1'].orientation_point = (LENGTH/2, HEIGTH/2, 0.0)

# create the modeling groupe for the plies
myGroup = myModel.create_modeling_group(name='Layers')

# create the plies
for i in range(stackup.shape[1]):
    myGroup.create_modeling_ply(name='Ply_'+str(i))
    myGroup.plies['Ply_'+str(i)].angle_1_field = myTable.columns['Ply'+str(i)]
    myGroup.plies['Ply_'+str(i)].draping = 'tabular_values'
    myGroup.plies['Ply_'+str(i)].ply_material = myFabric
    myGroup.plies['Ply_'+str(i)].oriented_selection_sets = (myModel.oriented_selection_sets['OrientedSelectionSet.1'])

    #if i > stackup.shape[1]:
    #    myGroup.create_interface_layer(name = 'interface'+str(i))
    #    myGroup.plies['InterfaceLayer.'+str(i)].oriented_selection_sets = (myModel.oriented_selection_sets['OrientedSelectionSet.1'])

# create the solid model
mySolid = myModel.create_solid_model( name='SolidModel.1' )
mySolid.connect_butt_joined_plies = False
mySolid.disable_dropoffs_on_top = True
mySolid.disable_dropoffs_on_bottom = True
mySolid.element_sets = (myElements)

# update a end of the script
myModel.update()

# save the model
myModel.save()


