
function AddProjectTemplateController($scope, $http, $location, $mdDialog) {
    var search_text = "";
    var selected_template;
    $scope.zoomValue = 4.5;

    $scope.init = function () {
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
        if (selected_template) {
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
                $scope.areas[i]['clips'] = [];
            }
            $scope.clip = "";
            $scope.selected_clips = [];
        }
    };

    $scope.save = function (selected_template, areas) {
        if (!validate(areas)) return;
        data = {
            "template_id": selected_template.id,
            "areas": areas
        };
        $http.post("projects/add_project_template/", data).success(function () {
            $location.path('/projects');
        });
    };

    var validate = function (areas) {
        if (areas == undefined) {
            alert("You need to select template first!");
            return false;
        }
        for (var i = 0; i < areas.length; i++) {
            if (!areas[i]['clips'].length) {
                alert("All areas must have clips!");
                return false;
            }
        }
        return true;
    };

    $scope.querySearch = function (query) {
        return query ? $scope.templates.filter(createFilterFor(query)) : $scope.templates;
    };

    var createFilterFor = function (query) {
        return function filterFn(template) {
            return (template.template_name.toLowerCase().indexOf(query.toLowerCase()) === 0);
        };
    };

    $scope.showDialog = function (ev) {
        var area_id = parseInt(ev.currentTarget.id)-1;
        if($scope.areas[area_id]['clips']) {
            $scope.selected_clips = $scope.areas[area_id]['clips'];
        }
        $mdDialog.show({
            controller: DialogController,
            templateUrl: 'static/js/app/projects/views/clip_add_dialog.html',
            parent: angular.element(document.body),
            targetEvent: ev,
            clickOutsideToClose: true,
            scope: $scope,
            preserveScope: true
        })
            .then(function (answer) {
                $scope.areas[area_id]['clips'] = answer;
                console.log($scope.areas);

            }, function () {
                $scope.status = 'You cancelled the dialog.';
            });
    };

    function DialogController($scope, $mdDialog) {


        $scope.cancel = function () {
            $mdDialog.cancel();
        };
        $scope.answer = function (answer) {
            $mdDialog.hide(answer);
        };
    };
};