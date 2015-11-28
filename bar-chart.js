(function () {
    var data = [4, 8, 12, 16, 23, 42];
    var x = d3.scale.sqrt().domain([0, d3.max(data)]).range([0, 820]);
    var chart = d3.select('.chart')
        .selectAll('div')
        .data(data)
        .enter()
        .append('div')
        .style('width', function (d) {
            return x(d) + 'px';
        })
        .style('font-size',function(d){
            return 14 + "px";
        })
        .text(function (d) {
            return d;
        });
    window.chart = chart;
})();
