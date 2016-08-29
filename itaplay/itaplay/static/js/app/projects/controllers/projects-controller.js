
function AddProjectTemplateController($scope, $http, $location) {
    var search_text = "";
    var selected_template;
    $scope.zoomValue = 4.5;

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

    $scope.parseTemplate = function (selected_template) {
        if(selected_template) {
            if (window.DOMParser) {
                parser = new DOMParser();
                xmlDoc = parser.parseFromString(selected_template.template_content, "text/xml");
            }
            else // Internet Explorer
            {
                xmlDoc = new ActiveXObject("Microsoft.XMLDOM");
                xmlDoc.async = false;
                xmlDoc.loadXML(selected_template.template_content);
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
                $scope.areas[i]['clip_id'] = "";
            }
            $scope.clip = "";
            $scope.area = "";
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

    $scope.save = function (selected_template, areas) {
        if(!validate(areas)) return;
        data = {"template_id": selected_template.id,
                "areas": $scope.areas};
        $http.post("projects/add_project_template/", data).success(function () {
          $location.path('/projects');
        });
    };

    var validate = function (areas) {
        if(areas==undefined){alert("You need to select template first!"); return false;}
        for(var i=0;i<areas.length;i++)
        {
            if(areas[i]['id']==""||areas[i]['clip_id']=="") {
                alert("All areas must have clips!");
                return false;
            }
        }
        return true;
    };

    $scope.querySearch = function (query) {
        return query ? $scope.templates.filter(createFilterFor(query)) : $scope.templates;
    };

    var createFilterFor = function(query) {
        return function filterFn(template) {
            return (template.template_name.toLowerCase().indexOf(query.toLowerCase()) === 0);
        };
    };
}