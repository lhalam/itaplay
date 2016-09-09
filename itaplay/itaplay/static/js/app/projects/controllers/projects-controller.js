
function AddProjectTemplateController ($scope,$routeParams, $http, $location, $mdDialog) {
    $scope.zoomValue = 4.5;
    $scope.project_id = $routeParams.project_id;
    $scope.init = function () {
        $http.get("api/projects/" + $scope.project_id + "/").then(function (response) {
            $scope.project = response.data;
        }, function(response) {
            console.log(response);
        });

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
        if (!validate(selected_template,areas)){ return;}
        data = {
            "project_id": $scope.project_id,
            "template_id": selected_template.id,
            "areas": areas
        };
        $http.post("api/projects/" + $scope.project_id + "/template/", data).success(function () {
            $location.path("/projects/id=" + $scope.project_id + "/");
        });
    };

    var validate = function (selected_template, areas) {
        if (selected_template==null) {
            showAlert("You need to select template first!");
            return false;
        }
        for (i = 0; i < areas.length; i+=1) {
            if (!areas[i].clips.length) {
                showAlert("All areas must have clips!");
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
        if($scope.areas[area_id].clips) {
            $scope.selected_clips = $scope.areas[area_id].clips;
        }
        $mdDialog.show({
            controller: DialogController,
            templateUrl: "static/js/app/projects/views/clip_add_dialog.html",
            parent: angular.element(document.body),
            targetEvent: ev,
            clickOutsideToClose: true,
            scope: $scope,
            preserveScope: true
        })
            .then(function (answer) {
                $scope.areas[area_id].clips = answer;
                console.log($scope.areas);

            }, function () {
                $scope.status = "You cancelled the dialog.";
            });
    };

    var showAlert = function(message) {
        $mdDialog.show(
          $mdDialog.alert()
            .clickOutsideToClose(true)
            .title("Something went wrong")
            .textContent(message)
            .ariaLabel("Alert Dialog Demo")
            .ok("Got it!")
        );
      };

    function DialogController ($scope, $mdDialog) {


        $scope.cancel = function () {
            $mdDialog.cancel();
        };
        $scope.answer = function (answer) {
            $mdDialog.hide(answer);
        };
    };
};

itaplay.controller('ProjectCtrl', function($scope, $http, $route) {
    $http.get("api/projects/")
            .then(function (response) {
                $scope.projects = response.data['results'];
            });

    $scope.delete = function (project) {
        $http.delete("api/projects/" + project.id + "/")
            .success(function () {
                $route.reload();
            });
    };
});

itaplay.controller('EditProjectCtrl', function ($scope, $http, $routeParams, $location, $mdDialog) {

    var id = $routeParams.project_id;

    $http.get("api/projects/" + id + "/")
        .then(function (response) {
            $scope.project = response.data;
        });
     $http.get("player/player_view/").then(function (response) {
      $scope.data= response.data;
     }, function(response) {
          console.log(response);
        $scope.data = "Something went wrong";
    });

    $scope.addPlayers = function ($event){
        $mdDialog.show({
        controller: DialogController,
        templateUrl:"static/js/app/projects/views/add_players.html",
        parent: angular.element(document.body),
        locals: {parent: $scope},
        targetEvent: $event,
        clickOutsideToClose:true,
    })
        .then(function (answer) {
                $scope.new_players = answer;
                console.log($scope.new_players);
        }, function() {
          $scope.status = 'You cancelled the dialog.';
        });
   };     
    $scope.addProjectToPlayers = function (project, new_players) {
        data ={
            "project" : project, 
            "players" : new_players
        };
        $http.put("api/projects_to_players/", data)
            .success(function () {
                $location.path('/projects');
            });
    };
    $scope.update = function (project) {
        $http.put("api/projects/" + project.id + "/", project)
            .success(function () {
                $location.path('/projects');
            });
    };

    $scope.delete = function (project) {
        $http.delete("api/projects/" + project.id + "/")
            .success(function () {
                $location.path('/projects');
            });
    };
    
});

itaplay.controller('AddProjectCtrl', function ($scope, $http, $location, $mdDialog) {
    
    $scope.addPlayers = function ($event){
        $mdDialog.show({
        controller: DialogController,
        templateUrl:"static/js/app/projects/views/add_players.html",
        parent: angular.element(document.body),
        locals: {parent: $scope},
        targetEvent: $event,
        clickOutsideToClose:true,
    })
        .then(function (answer) {
                $scope.players = answer;
                console.log($scope.players);
        }, function() {
          $scope.status = 'You cancelled the dialog.';
        });
   };     

    $scope.create = function (project, players) {
        project["players"]=players;
        $http.post("api/projects/", project)
            .success(function () {
                $location.path('/projects');
            });
    };
});

