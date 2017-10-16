angular.module('overstudio', ['ui.router'])
.config(function($stateProvider,$urlRouterProvider) {
  var homeState = {
    name: 'home',
    url: '/',
    templateUrl: '/about.html',
    controller: 'MainCtrl'
  }

  var worksState = {
    name: 'work',
    url: '/works',
    templateUrl: '/works.html',
    controller: 'WorksCtrl'
  }

  var contactState = {
    name: 'contact',
    url: '/contact',
    templateUrl: '/contact.html',
    controller: 'ContactCtrl'
  }

  $stateProvider.state(homeState);
  $stateProvider.state(worksState);
  $stateProvider.state(contactState);
  $urlRouterProvider.otherwise('/');
})
.controller('MainCtrl', ['$scope','$http', function($scope, $http) {


$scope.HasNotSubscribe = true; //Не подписався на хуях сидіть остався
$scope.subscriberName;
$scope.subscriberEmail;
$scope.subscribe = function() {

$scope.data = {name:$scope.subscriberName, to: $scope.subscriberEmail};

        
        
$.ajax({
	url: "/subscribeUser",
	type: "post",
	datatype:"json",
	data: $scope.data,
	success: function(response){
    console.log(response);
    console.log($scope.subscriberName);
        $scope.subscriberName = '';
        $scope.subscriberEmail = '';

    console.log($scope.subscriberName);
    console.log($scope.HasNotSubscribe);
	}
});


$http({
        method : "post",
        url : "/subscribeUser"
    }).then(function mySuccess(response) {
        $scope.subscriberName = '';
        $scope.subscriberEmail = '';
        $scope.formSubscribe.name.$touched = false;
    }, function myError(response) {
});

}
}])
.controller('ContactCtrl', ['$scope', function($scope) {

$scope.CustomerName;
$scope.CustomerEmail;
$scope.CustomerPhone;
$scope.CustomerLocation;
$scope.CustomerCompany;
$scope.CustomerTypeProject;
$scope.CustomerProjectDetails;
$scope.order = function() {

$scope.data = {CustomerName:$scope.CustomerName,CustomerEmail: $scope.CustomerEmail,CustomerPhone: $scope.CustomerPhone,CustomerLocation: $scope.CustomerLocation,CustomerCompany: $scope.CustomerCompany,CustomerTypeProject: $scope.CustomerTypeProject,CustomerProjectDetails: $scope.CustomerProjectDetails};


$.ajax({
  url: "/orderProject",
  type: "post",
  datatype:"json",
  data: $scope.data,
  success: function(response){
      console.log(response);
      $scope.CustomerName = '';
      $scope.CustomerEmail = '';
      $scope.CustomerPhone = '';
      $scope.CustomerLocation = '';
      $scope.CustomerCompany = '';
      $scope.CustomerTypeProject = '';
      $scope.CustomerProjectDetails = '';
  }
});

}
}])
.controller('WorksCtrl', ['$scope', function($scope) {

}]);




