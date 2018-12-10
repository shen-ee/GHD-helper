
var margin = ({top: 30, right: 150, bottom: 50, left: 150});
var w = 1400;
var h = 600;

var classes = ["stump_gunner", "snowflake", "tesla", "laser", "dj", "teleport", "tina", "petey", "compy", "bruno", "red_boss"];
var classes2 = ["power_of_tower", "power_of_monster"]
d3.csv("data.csv").then(function(dataset){

    var stack = d3.stack().keys(["stump_gunner", "snowflake", "tesla", "laser", "dj", "teleport", "tina", "petey", "compy", "bruno", "red_boss"]);
    var series = stack(dataset);
    // console.log(dataset);
    // console.log(series);
    var xScale = d3.scaleBand()
    .domain(d3.range(dataset.length))
    .range([margin.left, w-margin.right])
    // .paddingInner(0.05);
    var xScale2 = d3.scaleLinear()
    .domain([0,dataset.length])
    .range([margin.left, w-margin.right])

    dataset.sort(function(a, b) { return (+b.stump_gunner + +b.snowflake + +b.tesla + +b.laser + +b.dj + +b.teleport + +b.tina + +b.petey + +b.compy + +b.bruno + +b.red_boss) - (+a.stump_gunner + +a.snowflake + +a.tesla + +a.laser + +a.dj + +a.teleport + +a.tina + +a.petey + +a.compy + +a.bruno + +a.red_boss); });

    var yScale = d3.scaleLinear()
    .domain([0,				
        d3.max(dataset, function(d) {
            return +d.stump_gunner + +d.snowflake + +d.tesla + +d.laser + +d.dj + +d.teleport + +d.tina + +d.petey + +d.compy + +d.bruno + +d.red_boss;
        })
    ])
    .range([h-margin.bottom, margin.top]);

    				
    //Easy colors accessible via a 10-step ordinal scale
    var colors = d3.scaleOrdinal().domain(["stump_gunner", "snowflake", "tesla", "laser", "dj", "teleport", "tina", "petey", "compy", "bruno", "red_boss"])
    .range(["#FF6700", "#820933", "#B3679B", "#D7907B", "#E85D75", "#725752", "#3E92CC", "#18435A", "#96C0B7", "#2A628F", "#000000"]);

    //Create SVG element
    var svg = d3.select("#chart")
                .append("svg")
                .attr("width", w)
                .attr("height", h);

    // Add a group for each row of data
    var groups = svg.selectAll("g")
        .data(series)
        .enter()
        .append("g")
        .style("fill", function(d, i) {
            return colors(i);
        });

    var legends = svg.selectAll(".legendrect")
        .data(series)
        .enter()
        .append("rect")
        .attr("fill", function(d, i) {
            return colors(i);
        })
        .attr("x", function(d, i){
            if (i in d3.range(6)){
            return w-margin.right+5;
            }
        })
        .attr("y", function(d, i){
            return i%6 * 40 + 100;
        })
        .attr("height", 20)
        .attr("width", 40)
    var legend_labels = svg.selectAll(".legendlabel")
        .data(series)
        .enter()
        .append("text")
        .attr("x", function(d, i){
            if (i in d3.range(6)){
            return w-margin.right+45;
            }
            else{
                return 45;
            }})
        .attr("y", function(d, i){
            return i%6 * 40+15 + 100;
        })
        .text(function(d, i){
            return classes[i];
        })
        .attr("stroke", "black")
    // Add a rect for each data value
    var rects = groups.selectAll("rect")
        .data(function(d) { 
            return d; 
        })
        .enter()
        .append("rect")
        .attr("x", function(d, i) {
            return xScale(i);
        })
        .attr("y", function(d) {
            return yScale(d[1]);
        })
        .attr("height", function(d) {
            return yScale(d[0]) - yScale(d[1]);
        })
        .attr("width", xScale.bandwidth());
    svg.append('g')
        .attr('class', 'x axis')
        .attr("transform", "translate(0," + 550 + ")")
        .call(d3.axisBottom(xScale2))
    svg.selectAll(".tick text")
    .text(function(d,i){
        return Math.round(d3.select(this).text() * 5 / 30) +"s";
    })
    .attr("font-size", 14)
    svg.append('g')
        .attr("class", "y axis")
        .attr("transform", "translate(" + (margin.left) + ",0)")
        .call(d3.axisLeft(yScale))
})

d3.csv("power_t_m.csv").then(function(dataset){

    var stack = d3.stack().keys(["power_of_tower","power_of_monster"]);
    var series = stack(dataset);
    // console.log(dataset);
    // console.log(series);
    var xScale2 = d3.scaleBand()
    .domain(d3.range(dataset.length))
    .range([margin.left, w-margin.right])
    // .paddingInner(0.05);
    dataset.sort(function(a, b) { return (+b.power_of_tower+ +b.power_of_monster) - (+a.power_of_tower+ +a.power_of_monster); });
    var xScale3 = d3.scaleLinear()
    .domain([0,dataset.length])
    .range([margin.left, w-margin.right])
    var yScale2 = d3.scaleLinear()
    .domain([0,				
        d3.max(dataset, function(d) {
            return +d.power_of_tower + +d.power_of_monster;
        })
    ])
    .range([h-margin.bottom, margin.top]);

    				
    //Easy colors accessible via a 10-step ordinal scale
    var colors2 = d3.scaleOrdinal().domain(["power_of_tower", "power_of_monster"])
    .range(["red", "blue"]);

    //Create SVG element
    var svg = d3.select("#chart2")
                .append("svg")
                .attr("width", w)
                .attr("height", h);

    // Add a group for each row of data
    var groups = svg.selectAll("g")
        .data(series)
        .enter()
        .append("g")
        .style("fill", function(d, i) {
            return colors2(i);
        });

    var legends = svg.selectAll(".legendrect")
        .data(series)
        .enter()
        .append("rect")
        .attr("fill", function(d, i) {
            return colors2(i);
        })
        .attr("x", w-margin.right-50)
        .attr("y", function(d, i){
            return 100 - i * 40 ;
        })
        .attr("height", 20)
        .attr("width", 40)
    var legend_labels = svg.selectAll(".legendlabel")
        .data(series)
        .enter()
        .append("text")
        .attr("x", w-margin.right-10)
        .attr("y", function(d, i){
            return 15 + 100 - i * 40;
        })
        .text(function(d, i){
            return classes2[i];
        })
        .attr("stroke", "black")
    // Add a rect for each data value
    var rects = groups.selectAll("rect")
        .data(function(d) { 
            return d; 
        })
        .enter()
        .append("rect")
        .attr("x", function(d, i) {
            return xScale2(i);
        })
        .attr("y", function(d) {
            return yScale2(d[1]);
        })
        .attr("height", function(d) {
            return yScale2(d[0]) - yScale2(d[1]);
        })
        .attr("width", xScale2.bandwidth());

        svg.append('g')
        .attr('class', 'x axis')
        .attr("transform", "translate(0," + 550 + ")")
        .call(d3.axisBottom(xScale3))
    svg.selectAll(".tick text")
    .text(function(d,i){
        return Math.round(d3.select(this).text() * 5 / 30) +"s";
    })
    .attr("font-size", 14)
    svg.append('g')
        .attr("class", "y axis")
        .attr("transform", "translate(" + (margin.left) + ",0)")
        .call(d3.axisLeft(yScale2))
    
})