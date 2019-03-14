## Data Vis Tools and Tutorials
* [Google Fusion Tables](https://fusiontables.google.com) 
* [RAW](http://app.rawgraphs.io)  
* [DataWrapper](https://app.datawrapper.de)
* Benjamin Bach's list of [datavis tools](https://vishubblog.wordpress.com/tools/)
* Miriam Posner's list of [datavis tools](https://docs.google.com/document/d/1Z-14hgZPMIiAzT6vx1mVg5l60zkRVU9EHgZgK9HHdU4/edit#)

## Spatial Data, Maps and GIS
Mapping tools enable you to show data on a map and customise the map.
Some mapping systems allow you to extract data, others allow you to add to a public map

* [Mapbox Studio](https://studio.mapbox.com/)A free-to-use service that you can import data with geolocation information and create your own map.The base map is OSM, and there are a variety of other layers you can add too.
* [OpenStreetMap](http://www.openstreetmap.org) This is a open volunteer collected geographic information source that anyone can contrbute to and usethe data from.
* [Over-Pass Turbo](https://overpass-turbo.eu/) A free tool to extract data from OpenStreetmap, or visualise specific data in the database
** For example [Recycling points maped in Edinburgh](https://overpass-turbo.eu/map.html?Q=%2F*%0AThis%20has%20been%20generated%20by%20the%20overpass-turbo%20wizard.%0AThe%20original%20search%20was%3A%0A%E2%80%9Crecycling%E2%80%9D%0A*%2F%0A%5Bout%3Ajson%5D%5Btimeout%3A25%5D%3B%0A%2F%2F%20gather%20results%0A(%0A%20%20%2F%2F%20query%20part%20for%3A%20%E2%80%9Crecycling%E2%80%9D%0A%20%20node%5B%22amenity%22%3D%22recycling%22%5D(55.877429406597244%2C-3.3697128295898438%2C55.99857294657318%2C-3.0263900756835938)%3B%0A%20%20way%5B%22amenity%22%3D%22recycling%22%5D(55.877429406597244%2C-3.3697128295898438%2C55.99857294657318%2C-3.0263900756835938)%3B%0A%20%20relation%5B%22amenity%22%3D%22recycling%22%5D(55.877429406597244%2C-3.3697128295898438%2C55.99857294657318%2C-3.0263900756835938)%3B%0A)%3B%0A%2F%2F%20print%20results%0Aout%20body%3B%0A%3E%3B%0Aout%20skel%20qt%3B)  and [the code](https://overpass-turbo.eu/s/GZF)
* [GoogleMaps](https://www.google.com/maps/search/theatres/@55.9478499,-3.2118952,14z) contains lots of data, and you can create your own maps too
* [Leaflet](https://leafletjs.com/)  If you are putting maps on a web page and want to include your own data layer, Leaflet is a easy to use tool if you are able to edit web code.

Geographic Information Systems are much more comprehensive tools for handling geographic data. They handle things such as 'shapefiles", tranform different projects on to a map, and allow mathematical analysis of spatial features - such as density, clustering etc. today there are many open source tools that compete with commerical systems (e.g. ArcGIS)

* [Free GIS tools](https://gisgeography.com/free-gis-software/)

### Exercises
* Try to extract some data from OpenStreetMap using overpass
* Use one of the datasets on Datastore (under Class/mapping) or other data you have collected or found to create a mao on Mapbox
* Try Editing OSM directly.


