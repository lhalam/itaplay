function MonitorController($scope, $sce, $rootScope, $http, $routeParams,  $interval) {
    var mac = $routeParams.mac;
    $scope.init = function( ) {
        $http.get('get_by_mac/'+ mac).then(function(response) {
            if (window.DOMParser) {
                parser = new DOMParser();
                xmlDoc = parser.parseFromString(response.data.template, "text/xml");
            } else { // Internet Explorer

                xmlDoc = new ActiveXObject("Microsoft.XMLDOM");
                xmlDoc.async = false;
                xmlDoc.loadXML(response.data.template);
            }

            $scope.areas = [];
            DOM_areas = xmlDoc.getElementsByTagName("area");
            for (var i = 0; i < DOM_areas.length; i++) {
                $scope.areas[i] = {};
                $scope.areas[i]['id'] = DOM_areas[i].id;
                $scope.areas[i]['height'] = DOM_areas[i].attributes.height.nodeValue;
                $scope.areas[i]['width'] = DOM_areas[i].attributes.width.nodeValue;
                $scope.areas[i]['top'] = DOM_areas[i].attributes.top.nodeValue;
                $scope.areas[i]['left'] = DOM_areas[i].attributes.left.nodeValue;
                DOM_clip = DOM_areas[i].getElementsByTagName("clip");
                $scope.areas[i]['clips'] = [];
                for (var k = 0; k < DOM_clip.length; k++) {
                    $scope.areas[i]['clips'][k] = {};
                    $scope.areas[i]['clips'][k]['id'] = 'k';
                    $scope.areas[i]['clips'][k]['src'] = DOM_clip[k].attributes.src.nodeValue;
                    $scope.areas[i]['clips'][k]['mimetype'] = DOM_clip[k].attributes.mimetype.nodeValue;
                };
            };

            ImageSlider($scope.areas);
            VideoSlider($scope.areas);

        }, function(response) {
            console.log(response);
            $scope.data = "Something went wrong";
        });
    };

    $scope.trustSrc = function(src) {
                return $sce.trustAsResourceUrl(src);
            }

    $scope.currentIndex=[];
    $scope.currentVideoIndex = [];


    $scope.isCurrentSlideIndex = function (id_area, index) {
        return $scope.currentIndex[id_area] === index;
    };

    $scope.isCurrentSlideVideoIndex = function(id_area, index) {
        return $scope.currentVideoIndex[id_area] === index;
    };
    
    var VideoSlider = function(areas) {
        areas.forEach(function(area) {
          $scope.currentVideoIndex[area['id']] = 0;
          $interval(function(){$scope.currentVideoIndex[area['id']] = ($scope.currentVideoIndex[area['id']] < area['clips'].length - 1) ? ++$scope.currentVideoIndex[area['id']] : 0;}, 60000);
        });
    };

    var ImageSlider = function(areas){
        areas.forEach(function(area) {
          $scope.currentIndex[area['id']] = 0;
          $interval(function(){$scope.currentIndex[area['id']] = ($scope.currentIndex[area['id']] < area['clips'].length - 1) ? ++$scope.currentIndex[area['id']] : 0;}, 5000+area['id']*400);
        });
    };
};
