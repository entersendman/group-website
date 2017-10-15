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
.controller('MainCtrl', ['$scope', function($scope) {

$scope.HasSubscribe = false;
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

	    if (response["status"]=='subscribed') {
        $scope.HasSubscribe = true;
        $scope.subscriberName = '';
        $scope.subscriberEmail = '';
      }
	}
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
}]);


