function golfScore(par, strokes) {
  if(strokes == 1) {
    return "Hole-in-one!";
  } else if(strokes <= par - 2) {
    return "Eagle";
  } else if(strokes == par - 1) {
    return "Birdie";
  } else if(strokes == par) {
    return "Par";
  } else if(strokes == par + 1) {
    return "Bogey";
  } else if(strokes == par + 2) {
    return "Double Bogeu";
  } else {
    return "Do Home!";
  }
}

// Change these values to calculate
golfScore(5, 4);
