

var width = 1500,
    height = 1100,
    centered;

var projection = d3.geo.albersUsa()
    .scale(2000)
    .translate([760, height / 2]);

var path = d3.geo.path()
    .projection(projection);

var svg = d3.select("body").append("svg")
    .style("width", "100%")
    .style("height", "100%");


svg.append("rect")
    .attr("class", "background")
    .attr("width", width)
    .attr("height", height);
var g = svg.append("g");

// path data
d3.json({% static 'us.json' %}, function(unitedState) {
    console.log(unitedState);
  var data = topojson.feature(unitedState, unitedState.objects.states).features;
  // our names
  d3.tsv("us-states-names.tsv", function(tsv){
    // extract just the names and Ids
    var names = {};
    tsv.forEach(function(d,i){
      names[d.id] = d.name;
    });

    // build paths
g.append("g")
  .attr("class", "states-bundle")
  .selectAll("path")
  .data(data)
  .enter()
  .append("path")
  .attr("d", path)
  .attr("stroke", "white")
  .attr("class", "states");

 // add state names
 g.append("g")
  .attr("class", "states-names")
  .selectAll("text")
  .data(data)
  .enter()
  .append("svg:text")
  .text(function(d){
    return names[d.id];
  })
  .attr("x", function(d){
      return path.centroid(d)[0];
  })
  .attr("y", function(d){
      return  path.centroid(d)[1];
  })
  .attr("text-anchor","middle")
  .attr('fill', 'white');

});
});