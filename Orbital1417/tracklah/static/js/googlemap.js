//GLOBAL VARIABLES
var singapore = {
    lat: 1.3521,
    lng: 103.8198
}; //center of map

var optimalCenter= {
  lat: 11.4730946,
  lng: 104.4434885
};
//var iconFilePath= '/static/img/';
var iconDict = {
    "endSlaveryNow": "/static/img/img/childrenMarkerTransp.png",
    "sterileAnimals": "/static/img/img/dogMarkerTransp.png",
    "EdenReforestation": "/static/img/img/treeMarkerTransp.png",
    "emptyMarker": "/static/img/img/emptyMarkerTransp.png"
};


//list of marker objects
var markerObj = [];

//initalize map
function initMap() {
    console.log('inside googlemap js now');
    /* console.log(typeof(queryMarkerSubData[0].fields.lng)); */


    /*if there is NO user Input */

    if(userInput == 1){
      queryCenter= {lat : queryMarkerSubData[0].fields.lat,
                lng: queryMarkerSubData[0].fields.lng };

      var map= new google.maps.Map(document.getElementById('map'),{
        zoom: queryMarkerSubData[0].fields.zoom,
        center: queryCenter
      });
    }

    else{
        var map = new google.maps.Map(document.getElementById('map'), {
            zoom: 9,
            center: optimalCenter
        });
    }



    var iconImg;
    /* populating the map with all MARKERS */
    var infoWindow = new google.maps.InfoWindow(), marker, i;


    /*Custom Icon WIP */
    //console.log(queryMarkerSubData[0].fields.projectNameMain);
    /*
    for (var key in iconDict) {

        if (charityProjSubAllData[i].fields.projectNameMain == key) {
          console.log(charityProjSubAllData[i].fields.projectNameMain);
            iconPresent= true;
            iconImg = {
                url: iconDict[key],
                scaledSize: new google.maps.Size(30, 30),
                origin: new google.maps.Point(0, 0),
                anchor: new google.maps.Point(0, 0)
            };
        }
      }

      if(iconPresent== false){
        iconImg = {
            url: iconDict["emptyMarker"],
            scaledSize: new google.maps.Size(30, 30),
            origin: new google.maps.Point(0, 0),
            anchor: new google.maps.Point(0, 0)
          }
        }
      console.log(iconPresent);
*/

    for (i = 0; i < charityProjSubAllData.length; i++) {
      var iconPresent= false;
      for (var key in iconDict) {

          if (charityProjSubAllData[i].fields.projectNameMain == key) {
            console.log(charityProjSubAllData[i].fields.projectNameMain);
              iconPresent= true;
              iconImg = {
                  url: iconDict[key],
                  scaledSize: new google.maps.Size(30, 30),
                  origin: new google.maps.Point(0, 0),
                  anchor: new google.maps.Point(0, 0)
              };
          }
        }

        if(iconPresent== false){
          iconImg = {
              url: iconDict["emptyMarker"],
              scaledSize: new google.maps.Size(30, 30),
              origin: new google.maps.Point(0, 0),
              anchor: new google.maps.Point(0, 0)
            }
          }
        console.log(iconPresent);


        var marker = new google.maps.Marker({

            position: new google.maps.LatLng(charityProjSubAllData[i].fields.lat, charityProjSubAllData[i].fields.lng),
            map: map,
            title: charityProjSubAllData[i].fields.projectNameSub,
            charityName:charityProjSubAllData[i].fields.charityName,
            icon: iconImg

            });
        //var contentpage = '<h2> test </h2><img src= "/static/img/sterileAnimal1.jpg">' + charityProjSubAllData[i].fields.infoWindowWriteup
        if(userInput==1  &&
            queryMarkerSubData[0].fields.lat == charityProjSubAllData[i].fields.lat &&
            queryMarkerSubData[0].fields.lng == charityProjSubAllData[i].fields.lng
          ){
          infoWindow.setContent(charityProjSubAllData[i].fields.infoWindowWriteup);
          infoWindow.open(map,marker);

        }

        google.maps.event.addListener(marker, 'click', (function(marker, i) {
           return function() {
               infoWindow.setContent(charityProjSubAllData[i].fields.infoWindowWriteup);
               infoWindow.open(map, marker);

           }
       })(marker, i));



       /*
        var infoWindow = new google.maps.InfoWindow({
          //content: contentpage
          content: charityProjSubAllData[i].fields.infoWindowWriteup
        });
        console.log(charityProjSubAllData[i].fields.infoWindowWriteup);



        // to show infoWindow for queried markers
        if(userInput==1  &&
            queryMarkerSubData[0].fields.lat == charityProjSubAllData[i].fields.lat &&
            queryMarkerSubData[0].fields.lng == charityProjSubAllData[i].fields.lng
          ){

          infoWindow.open(map,marker);
        }
        //show descript when clicked
        google.maps.event.addListener(marker, 'click', (function(marker, i) {
            return function() {
                infoWindow.open(map, marker);
            }
        })(marker, i));
        */

        //markerObj.push(marker);
    }


    /*
    //filtering markers according to charity organ when clicked
    for (j = 0; j < markerObj.length; j++) {
        google.maps.event.addListener(markerObj[j], 'dblclick', (function(marker, j) {
            return function() {
                for (i = 0; i < markerObj.length; i++) {

                    if (j == i) {
                        continue;
                    }
                    if (markerObj[i].charityName != markerObj[j].charityName) {
                        markerObj[i].setVisible(false);
                    }
                }
            }
        })(marker, j));
    }
    */
    //custom icon for different charity organ during initial load

    /*
    //map recentering function
    var centerControlDiv = document.createElement('div');
    var centerControl = new CenterControl(centerControlDiv, map);
    centerControlDiv.index = 1;
    map.controls[google.maps.ControlPosition.TOP_RIGHT].push(centerControlDiv);


    //reset all filters
    var controlfilter = document.createElement('div');
    var resetFilter = new ResetFilter(controlfilter, map);
    controlfilter.index = 1;
    map.controls[google.maps.ControlPosition.RIGHT_TOP].push(controlfilter);


    //donation code to charity project location
    //need to think about resizing the boundaries and to hide the pins if the zoom is too high
    var inputChocoCode = document.getElementById('codeInput').value;
    console.log("ChocoCode is >>>>>> "+ inputChocoCode);

    if(inputChocoCode!=null){

      for(i=0;i<charityProjSubAllData.length;i++){
        console.log(charityProjSubAllData[i].fields.chocoCode);
        if(charityProjSubAllData[i].fields.chocoCode==inputChocoCode){
          //var recenter={charityProjSubAllData[i].fields.lat}
          var newlat= parseFloat(charityProjSubAllData[i].fields.lat);
          var newlng= parseFloat(charityProjSubAllData[i].fields.lng);
          console.log(newlat);

        }

      }
      var recenter= {lat : newlat, lng : newlng};
      map.panTo(recenter);
    }
    */

}

/*
function CenterControl(controlDiv, map) {

    // Set CSS for the control border.
    var controlUI = document.createElement('div');
    controlUI.style.backgroundColor = '#fff';
    controlUI.style.border = '2px solid #fff';
    controlUI.style.borderRadius = '3px';
    controlUI.style.boxShadow = '0 2px 6px rgba(0,0,0,.3)';
    controlUI.style.cursor = 'pointer';
    controlUI.style.marginBottom = '22px';
    controlUI.style.textAlign = 'center';
    controlUI.title = 'Click to recenter the map';
    controlDiv.appendChild(controlUI);

    // Set CSS for the control interior.
    var controlText = document.createElement('div');
    controlText.style.color = 'rgb(25,25,25)';
    controlText.style.fontFamily = 'Roboto,Arial,sans-serif';
    controlText.style.fontSize = '16px';
    controlText.style.lineHeight = '38px';
    controlText.style.paddingLeft = '5px';
    controlText.style.paddingRight = '5px';
    controlText.innerHTML = 'Center Map';
    controlUI.appendChild(controlText);

    // Setup the click event listeners: simply set the map to Chicago.
    controlUI.addEventListener('click', function() {
        map.panTo(singapore);
        map.setZoom(11);

    });

}

function ResetFilter(controlfilter, map) {

    // Set CSS for the control border.
    var controlUI = document.createElement('div');
    controlUI.style.backgroundColor = '#fff';
    controlUI.style.border = '2px solid #fff';
    controlUI.style.borderRadius = '3px';
    controlUI.style.boxShadow = '0 2px 6px rgba(0,0,0,.3)';
    controlUI.style.cursor = 'pointer';
    controlUI.style.marginBottom = '22px';
    controlUI.style.textAlign = 'center';
    controlUI.title = 'Click to see all Charity Projects';
    controlfilter.appendChild(controlUI);

    // Set CSS for the control interior.
    var controlText = document.createElement('div');
    controlText.style.color = 'rgb(25,25,25)';
    controlText.style.fontFamily = 'Roboto,Arial,sans-serif';
    controlText.style.fontSize = '16px';
    controlText.style.lineHeight = '38px';
    controlText.style.paddingLeft = '5px';
    controlText.style.paddingRight = '5px';
    controlText.innerHTML = 'All Charity Projects';
    controlUI.appendChild(controlText);

    // Setup the click event listeners: simply set the map to Chicago.
    controlUI.addEventListener('click', function() {
        for (i = 0; i < markerObj.length; i++) {
            markerObj[i].setVisible(true);
            map.panTo(singapore);
            map.setZoom(11);
        }

    });

}
*/
