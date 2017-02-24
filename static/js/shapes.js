var s = Snap('100%', 700 );
var style = {
    fill: '#ff6ff6',
    stroke: '#ffeead',
    strokeWidth: 10
};
var circle =s.circle(100,100,50).attr(style);
var rect = s.rect(200,50,100,100).attr(style);

var ellipse = s.ellipse(400,100,70,40).attr(style);

var line = s.line(100,100,300,300).attr({stroke: 'red', strokeWidth: 10});

// var polyline = s
//     .polyline(700, 100, 650, 200,700, 300)
//     .attr({stroke: 'red', strokeWidth: 10});

var polygon = s
    .polygon(700, 100, 650, 200,700, 300)
    .attr({
        stroke: 'red',
        strokeWidth: 10,
        fill: 'transparent'
    });

var path = s
    .path("M100 200L200 250")
    .attr({
        stroke: "blue",
        strokeWidth: 10
    });

// M  moveto  (x y)+
// Z  closepath  (none)
// L  lineto  (x y)+
// H  horizontal lineto  x+
// V  vertical lineto  y+
// C  curveto  (x1 y1 x2 y2 x y)+
// S  smooth curveto  (x2 y2 x y)+
// Q  quadratic Bézier curveto  (x1 y1 x y)+
// T  smooth quadratic Bézier curveto  (x y)+
// A  elliptical arc  (rx ry x-axis-rotation large-arc-flag sweep-flag x y)+



circle.animate(
    {
        r: '70'
    },
    300,
    mina.elastic
);

// rect.drag(
//     function (dx) {
//         console.log(dx);
//     }
// );

rect.transform('r45, 250, 100');


var ball = s
    .circle(200, 500, 40)
    .attr(style)
    .mouseover(function () {
        return this.animate(
            {
                cx: 500
            }, 800, mina.elastic
        )
    })
    .click(function () {
        return this.animate(
            {
                cx: 100
            }, 800, mina.easeinout
        )
    });

