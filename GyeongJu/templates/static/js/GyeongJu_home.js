const region_list = ['gyeongju', 'suncheon', 'jeonju', 'language'];
var rect_position = {};

for (var i = 0; i < region_list.length; i++) {
  var element = document.getElementById(region_list[i]);
  var rect = element.getBoundingClientRect();

  if (!rect_position[region_list[i]]) {
    rect_position[region_list[i]] = [];
  }
  rect_position[region_list[i]] = [rect.top, rect.left];
}
console.log(rect_position);

var elements = document.querySelectorAll('.d');

elements.forEach(function (element) {
  element.addEventListener('mouseover', function () {
    var region_name = element.id;
    var column_name = region_name + '_column';
    console.log(column_name);
    var dropDown = document.getElementById(column_name);

    var percentageX = (rect_position[region_name][1] / window.innerWidth) * 100;
    dropDown.style.position = 'relative';
    dropDown.style.left = percentageX - 0.9 + '%';
  });
});
