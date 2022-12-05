var graph = new Rickshaw.Graph({
  stroke: true,
  width: 70,
  series: [
    {
      color: 'lightblue',
      data: [
        { x: 0, y: 0 },
        { x: 1, y: 0 },
        { x: 2, y: 30 },
        { x: 3, y: 40 },
      ],
    },
  ],
  renderer: 'area',
  element: document.querySelector('#chart'),
});

graph.render();

var graph = new Rickshaw.Graph({
  stroke: true,
  width: 70,
  series: [
    {
      color: 'lightblue',
      data: [
        { x: 1, y: 0 },
        { x: 2, y: 5 },
        { x: 3, y: 2 },
        { x: 4, y: 2 },
        { x: 5, y: 3 },
        { x: 6, y: 0 },
      ],
    },
  ],
  renderer: 'area',
  element: document.querySelector('#activity'),
});

graph.render();

var graph = new Rickshaw.Graph({
  stroke: true,
  width: 70,
  series: [
    {
      color: 'tomato',
      data: [
        { x: 0, y: 4 },
        { x: 1, y: 3 },
        { x: 3, y: 0 },
        { x: 4, y: 0 },
      ],
    },
  ],
  renderer: 'area',
  element: document.querySelector('#project'),
});

graph.render();

var graph = new Rickshaw.Graph({
  stroke: true,
  width: 70,
  series: [
    {
      color: 'green',
      data: [
        { x: 1, y: 2 },
        { x: 2, y: 2 },
        { x: 3, y: 4 },
        { x: 4, y: 4 },
      ],
    },
  ],
  renderer: 'area',
  element: document.querySelector('#todayworkedChart'),
});

graph.render();

var graph = new Rickshaw.Graph({
  stroke: true,
  width: 70,
  series: [
    {
      color: 'green',
      data: [
        { x: 1, y: 1 },
        { x: 2, y: 2 },
        { x: 3, y: 3 },
        { x: 4, y: 4 },
      ],
    },
  ],
  renderer: 'area',
  element: document.querySelector('#todayChart'),
});

graph.render();

let nullgraph = document.querySelectorAll('.nullgraph');
for (let item of nullgraph) {
  var graph = new Rickshaw.Graph({
    stroke: true,
    width: 70,
    series: [
      {
        color: 'lightgray',
        data: [
          { x: 0, y: 0 },
          { x: 1, y: 1 },
          { x: 2, y: 1 },
          { x: 3, y: 2 },
          { x: 4, y: 2 },
          { x: 5, y: 3 },
          { x: 6, y: 3 },
        ],
      },
    ],
    renderer: 'area',
    element: item,
  });

  graph.render();
}
