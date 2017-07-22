//GLOBAL VARIABLES
var singapore = {
    lat: 1.3521,
    lng: 103.8198
}; //center of map

// sample data, global variable
/*
var markerslist = [
    ['eusoffexpeds', 1.2940, 103.7705, "kalaidescope", "nus"],
    ['shearesHall', 1.2914, 103.7756, "idk2", "nus"],
    ['hall1', 1.3453, 103.6873, "idk3", "ntu"],
    ['hall10', 1.3543, 103.6857, "idk4", "ntu"],
    ['smuHall1', 1.292165498, 103.842663296, 'idk5', "smu"],
    ['sutd', 1.3403, 103.9629, "idk6", "sutd"]
];
*/

/*
var infoWindowContent = [
    ['<div class="info_content">' +
        '<h3>EusoffHall</h3>' +
        '<p>The London Eye is a giant Ferris wheel situated on the banks of the River Thames. The entire structure is 135 metres (443 ft) tall and the wheel has a diameter of 120 metres (394 ft).</p>' + '</div>'
    ],
    ['<div class="info_content">' +
        '<h3>shearesHall</h3>' +
        '<p>The Palace of Westminster is the meeting place of the House of Commons and the House of Lords, the two houses of the Parliament of the United Kingdom. Commonly known as the Houses of Parliament after its tenants.</p>' +
        '</div>'
    ],
    ['<div class="info_content">' +
        '<h3>Hall1</h3>' +
        '<p>The London Eye is a giant Ferris wheel situated on the banks of the River Thames. The entire structure is 135 metres (443 ft) tall and the wheel has a diameter of 120 metres (394 ft).</p>' + '</div>'
    ],
    ['<div class="info_content">' +
        '<h3>Hall10</h3>' +
        '<p>The Palace of Westminster is the meeting place of the House of Commons and the House of Lords, the two houses of the Parliament of the United Kingdom. Commonly known as the Houses of Parliament after its tenants.</p>' +
        '</div>'
    ],
    ['<div class="info_content">' +
        '<h3>smuHall1</h3>' +
        '<p>The London Eye is a giant Ferris wheel situated on the banks of the River Thames. The entire structure is 135 metres (443 ft) tall and the wheel has a diameter of 120 metres (394 ft).</p>' + '</div>'
    ],
    ['<div class="info_content">' +
        '<h3>sutd</h3>' +
        '<p>The Palace of Westminster is the meeting place of the House of Commons and the House of Lords, the two houses of the Parliament of the United Kingdom. Commonly known as the Houses of Parliament after its tenants.</p>' +
        '</div>'
    ]
];
*/

//var iconFilePath= '/static/img/';
var iconDict = {
    "nus": "/static/img/nusLogo.jpg",
    "ntu": "/static/img/ntuLogo.png",
    "smu": "/static/img/smuLogo.png",
    "sutd": "/static/img/sutdLogo.png"
};


//list of marker objects
var markerObj = [];

//initalize map
function initMap() {

    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 11,
        center: singapore
    });

    var infoWindow = new google.maps.InfoWindow(),
        marker, i;

    var iconImg;

    for (i = 0; i < CharityProjectsData.length; i++) {
        var position = new google.maps.LatLng(CharityProjectsData[i].fields.lat, CharityProjectsData[i].fields.lng);

        for (var key in iconDict) {
            if (CharityProjectsData[i].fields.charityName == key) {
                iconImg = {
                    url: iconDict[key],
                    scaledSize: new google.maps.Size(30, 30),
                    origin: new google.maps.Point(0, 0),
                    anchor: new google.maps.Point(0, 0)
                };
            }

            var marker = new google.maps.Marker({
                position: position,
                map: map,
                title: CharityProjectsData[i].fields.projectName,
                charityName:CharityProjectsData[i].fields.charityName,
                icon: iconImg

                });
            //show descript when clicked
            google.maps.event.addListener(marker, 'click', (function(marker, i) {
                return function() {
                    infoWindow.setContent(CharityProjectsData[i].fields.shortDescrip);
                    infoWindow.open(map, marker);
                }
            })(marker, i));

            markerObj.push(marker);

        }
    }

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

    //custom icon for different charity organ during initial load


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

      for(i=0;i<CharityProjectsData.length;i++){
        console.log(CharityProjectsData[i].fields.chocoCode);
        if(CharityProjectsData[i].fields.chocoCode==inputChocoCode){
          //var recenter={CharityProjectsData[i].fields.lat}
          var newlat= parseFloat(CharityProjectsData[i].fields.lat);
          var newlng= parseFloat(CharityProjectsData[i].fields.lng);

        }

      }
      var recenter= {lat : newlat, lng : newlng};
      map.panTo(recenter);
    }


}


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
