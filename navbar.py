import dash_bootstrap_components as dbc

def Navbar():
        navbar = dbc.NavbarSimple(
           children=[
             # dbc.NavItem(dbc.NavLink("Column1", href="/Column1")),
              dbc.DropdownMenu(
                 nav=True,
                 in_navbar=True,
                 label="Menu",
                 children=[
                    dbc.DropdownMenuItem(divider=True),
                    dbc.DropdownMenuItem("Visualisation",disabled=True),

                    dbc.DropdownMenuItem(divider=True),

                    dbc.DropdownMenuItem("Visualisation des Cryptomonnaies",href="/Column1"),
                    #dbc.DropdownMenuItem("Courbe : Risque",href="/Column2"),
                    dbc.DropdownMenuItem(divider=True),
                    dbc.DropdownMenuItem("ML",disabled=True),
                    dbc.DropdownMenuItem(divider=True),

                    #dbc.DropdownMenuItem("Choix de cluster",href="/Column3"),
                    dbc.DropdownMenuItem("Modèle de prédiction",href="/Column4"),
                          ],
                      ),
                    ],
          brand="Home",
          brand_href="/home",
          sticky="top",
          id="navbar",
          color="gray",
        )


        return navbar

def Navbar_midle(name,color,pathname,barename):
        children = []
        for index in range(len(pathname)) :
            children.append(dbc.NavItem(dbc.NavLink(barename[index], href=pathname[index])))
        navbar = dbc.NavbarSimple(
        children=children,
        brand=name,
        brand_href="/home",
          #sticky="bottom",
        id="navbar",
        color = color,
        dark = True,
        )


        return navbar
