var count = 0;

// Calculate the running count
function cc(card) {
  switch (card) {
    case 2:
    case 3:
    case 4:
    case 5:
    case 6:
      count = count + 1;
      break;
    case 7:
    case 8:
    case 9:
      count = count;
      break;
    case 10:
    case 'J':
    case 'Q':
    case 'K':
    case 'A':
      count = count-1;
      break;
  }
  // Decide to "Bet" or "Hold"
  if (count > 0){
    return count + " Bet";
  } else {
    return count + " Hold";
  }
}

// Test your cards here
cc(2); cc(3); cc(7); cc('K'); cc('A');
