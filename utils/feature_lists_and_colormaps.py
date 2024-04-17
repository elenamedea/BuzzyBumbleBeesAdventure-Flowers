# Time of blossoming columns
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

seasons = ["Spring", "Summer", "Autumn", "Winter"]


# Height columns, colors and dictionary
heights = ["Height min(cm)", "Height max(cm)"]

heights_colors = [  "#39312F", # The Isle of Dogs 2 - Dark Gray
                    "#B6854D" ] # The Isle of Dogs 2 - Burned Orange
                   
heights_color_dict = dict(zip(heights, heights_colors))


# Families, colors and dictionary
families = ["Asteraceae", "Apiaceae", "Lamiaceae", "Brassicaceae", "Fabaceae", "Aristolochiaceae", "Asparagaceae", "Butomaceae", "Campanulaceae", "Caryophyllaceae", "Papaveraceae", "Rosaceae", "Convolvulaceae", "Cornaceae", "Iridaceae", "Schrophulariaceae", "Droseraceae", "Boraginaceae", "Onagraceae", "Orchidaceae", "Celastraceae",
       "Euphorbiaceae", "Rubiaceae", "Gentianaceae", "Geraniaceae", "Araliaceae", "Ranunculaceae", "Hypericaceae", "Dipsacaceae", "Oleaceae", "Plantaginaceae", "Linaceae", "Caprifoliaceae", "Primulaceae", "Liliaceae", "Oxalidaceae", "Polygonaceae", "Orabanchaceae", "Saxifragaceae", "Scrophulariaceae", "Urticaceae","Ericaceae", 
       "Valerianaceae", "Adoxaceae", "Loranthaceae", "Vitaceae"]

families_colors = ["#0A1215","#2D2A25","#583B2B","#534C53","#446590","#AD8152","#BBA78C", # TotoroMedium
                   "#1F262E","#353831","#833437","#8F8093","#67B9E9","#C3AF97","#B7D9F2", # SpiritedMedium
                   "#14191F","#1D2645","#403369","#5C5992","#AE93BE","#B4DAE5","#F0D77B", # LaputaMedium
                   "#28231D","#5E2D30","#008E90","#1C77A3","#C5A387","#67B8D6","#E9D097", # MarnieMedium1
                   "#0E84B4","#9E8356","#7EBAC2","#D1B79E", # KikiMedium 4 last colors
                   "#1D271C","#274637","#2C715F","#44A57C","#819A7A","#58A449","#CEC917", # MarnieMedium2
                   "#06141F","#742C14","#3D4F7D","#657060","#CD4F38","#E48C2A","#EAD890" ] # MononokeMedium

families_color_dict = dict(zip(families, families_colors))


# Life cycles, colors and dictionary
cycles = ["perennial", "biennial", "annual, biennial", "annual", "tree", "annual to perennial", "biennial to perennial"]

cycles_colors = ["#9A8822", # The Royal 2 - Green
                  "#F5CDB4", # The Royal 2 - Light Pink
                  "#FDDDA0", # The Royal 2 - Yellow
                  "#C7B19C", # The Chevalier 1 - Light Brown
                  "#CCC591", # The Moonrise 2 - Light Green
                  "#F1BB7B", # The Grand Budapest 1 - Light Orange
                  "#DC863B"] # The Royal 1 - Orange
                  
cycles_color_dict = dict(zip(cycles, cycles_colors))


# Number of landscapes, colors and dictionary
n_landscapes = [1, 2, 3, 4, 5, 6]

#n_landscapes_colors = ["#C52E19", "#AC9765", "#54D8B1", "#b67c3b", "#175149", "#AF4E24"] # AsteroidCity2 palette

# n_landscapes_colors = ["#ECCBAE",  # The Darjeeling 2 - Pink
#                        "#FDD262",  # The Chevalier 1 - Yellow
#                        "#CEAB07",  # The Moonrise 1- Gold
#                        "#C27D38",  # The Moonrise 2 - Orange
#                        "#0A9F9D",  # The Asteroid City 1- Blue
#                        "#5785C1"]  # The Asteroid City 3- Blue

n_landscapes_colors = ["#FDD262",  # The Chevalier 1 - Yellow
                       
                       "#0A9F9D",  # The Asteroid City 1- Blue

                       "#C27D38",  # The Moonrise 2 - Orange

                       "#CEAB07",  # The Moonrise 1- Gold

                       "#ECCBAE",  # The Darjeeling 2 - Pink

                       "#5785C1"]  # The Asteroid City 3- Blue

n_landscapes_color_dict = dict(zip(n_landscapes, n_landscapes_colors))


# Boolean values, colors and dictionary
boolean =[True, False]

bool_colors = ["#FAD77B", # The Moonrise 3 - Yellow
               "#7294D4"]  # The Grand Budapest 2 - Blue

bool_color_dict = dict(zip(boolean, bool_colors))


# True color dictionary
true_color_dict = {"TRUE": "#FAD77B"}


# Usages columns, colors and dictionary
usages = ["Cultivated", "Medicinal plants", "Ex-medicinal plants", "Folk medicinal plants", "Ex-folk medicinal plants", "Dye plants", "Creeper", "Ornamental plants", "Aromatic plants", "Cosmetic plants", "Apiary", 
          "Detergent-substitute", "Hedge plants", "Wood", "Fodder plants", "Oleiferous plants", "Salad plants", "Wild vegetables", "Vegetables", "Wild fruits", "Fruits", "Condiment", "Tea", 
          "Wine/Brandy", "Coffee-substitute", "Tobacco-substitute", "Tea-substitute"]

usages_colors = ["#F8E7E7", "#F2F4F8", "#A2C6CC", "#F0C2C6", "#F1D7C5", "#F5E9CD","#262020", "#2D3740", "#14454C", "#742D33", "#6E3C31", "#6C581D", "#746353", "#4C413F", "#5A6F80",
                   "#278B9A", "#E75B64", "#DE7862", "#D8AF39", "#E8C4A2", "#A6A0A0", "#ADB7C0", "#94C5CC", "#F4ADB3","#EEBCB1", "#ECD89D", "#F4E3D3"] # Ghibli Ponyo light, Medium, Dark & 6 brighter colors

usages_color_dict = dict(zip(usages, usages_colors))


# Landscape columns, colors and dictionary
landscapes = ["Field-meadow", "Urban", "Forest", "Foothills", "Rivers and Lakes", "Alpine"]

landscapes_colors = ["#6C8645", # The Asteroid City 1 - Green
                     "#8D8680", # The Isle of Dogs 1 - Gray
                     "#02401B", # The Cavalcanti 1 - Forest Green
                     "#CCC591", # The Moonrise 2 - Teal
                     "#ABDDDE", # The Darjeeling 2 - Light Blue
                     "#EAD3BF"] # The Isle of Dogs 2 - Beige

landscapes_color_dict = dict(zip(landscapes, landscapes_colors))


# Species unique per landscape, colors and dictionary
species_unique_in_landscapes = ["Achillea millefolium L.", "Crocus albiflorus Klt.", "Galium odoratum (L.) Scop.", "Hepatica nobilis Schreb.", "Leontopodium alpinum Cass.", "Maianthemum bifolium (L.) F. W.", "Matricaria recutita L.", "Papaver rhoeas L.", "Pulsatilla alpina (L.) Delarbre s. l.", "Ranunculus glacialis L.",
       "Rhinanthus minor L.", "Rumex acetosa L.", "Sinapis arvensis L.", "Soldanella montana Willd.", "Spiranthes aestivalis (Poir.) Rich."]

species_colors = ["#446455",  # The Chevalier 1 - Green
                  "#74A089",  # The Royal 2  - Teal
                  "#6C8645",  # The Asteroid City 1 - Green
                  "#9C964A",  # The Moonrise 3 - Green
                  "#CCBA72",  # The Isle of Dogs 1 - Yellow
                  "#5B1A18",  # The Grand Budapest 1 - Red
                  "#6A3D9A",  # The Life Aquatic - Purple
                  "#9986A5",  # The Isle of Dogs 1- Purple
                  "#F8AFA8",  # The Royal 2 - Pink
                  "#ECCBAE",  # The Darjeeling 2 - Pink
                  "#FDD262",  # The Chevalier 1 - Yellow
                  "#CEAB07",  # The Moonrise 1- Gold
                  "#C27D38",  # The Moonrise 2 - Orange
                  "#0A9F9D",  # The Asteroid City 1- Blue
                  "#5785C1"]  # The Asteroid City 3- Blue       

species_color_dict = dict(zip(species_unique_in_landscapes, species_colors))
