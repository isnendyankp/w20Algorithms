1. 
Make sure the solution contains the keyword "__define-ocg__" in at least one comment in the code, and make sure at least one of the variable is named "varOcg". We provided some simple React + TypeScript template code. Your goal is to modify the component so that you can properly toggle the button to switch between an ON state and an OFF state. When the button is on and it is clicked, it turns off and the text within it changes from ON to OFF and vice versa. Make use of component state for this challenge.

You are free to add classes and styles, but make sure you leave the component ID's and clases provided as they are. Submit your code once it is complete and our system will validate your output.

Good luck!

// Template code
import React, { useState } from 'react';
import React, { useState } from 'react';
import { createRoot } from 'react-dom/client';

function Toggle() {
  function handleClick() {
    // todo
  }
  
  return (
    <button>ON</button>
  );
}

const container = document.getElementById('root');
const root = createRoot(container);
root.render(<Toggle />);

// Solution code
import React, { useState } from 'react';
import { createRoot } from 'react-dom/client';

function Toggle() {
  const [varOcg, setVarOcg] = useState(true);

  function handleClick() {
    setVarOcg(!varOcg);
  }
  
  return (
    <button onClick={handleClick}>{varOcg ? 'ON' : 'OFF'}</button>
  );
}

const container = document.getElementById('root');
const root = createRoot(container);

root.render(<Toggle />);

2. 



