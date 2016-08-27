
function AddProjectTemplateController($scope, $http, $location) {

    $scope.init = function() {
        $http.get("/templates/all/").then(function (response) {
            $scope.templates = response.data;
        }, function (response) {
            console.log(response);
            $scope.data = "Something went wrong";
        });

        $http.get("/clips/clips/").then(function (response) {
            $scope.clips = response.data;
        }, function (response) {
            console.log(response);
            $scope.data = "Something went wrong";
        });
    };

    $scope.parseTemplate = function () {
        if (window.DOMParser)
        {
            parser = new DOMParser();
            xmlDoc = parser.parseFromString($scope.template.template_content, "text/xml");
        }
        else // Internet Explorer
        {
            xmlDoc = new ActiveXObject("Microsoft.XMLDOM");
            xmlDoc.async = false;
            xmlDoc.loadXML(txt);
        }
        $scope.areas=[];
        DOM_areas = xmlDoc.getElementsByTagName("area");
        for(var i=0; i<DOM_areas.length; i++)
        {
            $scope.areas[i] = {};
            $scope.areas[i]['id'] = DOM_areas[i].id;
            $scope.areas[i]['clip_id'] = "";
        }
    };

    $scope.assignClip = function() {
        $scope.areas[$scope.areas.indexOf($scope.area)]['clip_id'] = $scope.clip.pk;
  };

    $scope.chooseClip = function() {
        $scope.clip = $scope.findClipByID($scope.areas[$scope.areas.indexOf($scope.area)]['clip_id'])
  };

    $scope.findClipByID = function (id) {
        for(var i=0;i<$scope.clips.length;i++)
        {
            if($scope.clips[i].pk === id) return $scope.clips[i];
        }
    };
}