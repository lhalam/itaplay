function MonitorController($scope, $http, $routeParams) {
    var mac = $routeParams.mac;
    $scope.init = function( ) {
        $http.get('get_by_mac/'+ mac).then(function(response) {
            if (window.DOMParser) {
                parser = new DOMParser();
                xmlDoc = parser.parseFromString(response.data.template, "text/xml");
                }
            else { // Internet Explorer

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
                    $scope.areas[i]['clips'][k]['src'] = DOM_clip[k].attributes.src.nodeValue;
                };
            };
        }, function(response) {
            console.log(response);
            $scope.data = "Something went wrong";
        });
    };

    $scope.checkImage = function(value) {
        console.log("checkImage", value);
        var format = value.split('.').pop();
        return ['jpg', 'img', 'png', 'gif'].includes(format) ? true : false

    };

    $scope.checkVideo = function(value) {
        var format = value.split('.').pop();
        return ['mp4', 'avi', 'asf', 'flv'].includes(format) ? true : false
    };

};