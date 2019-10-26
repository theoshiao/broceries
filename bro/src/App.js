import React from 'react';
import AddBro from './AddBro.js'

import logo from './logo.svg';
import './App.css';


class App extends React.Component {
  constructor () {
    super();
  }

  render() {
    return (
      <div className="App">
        <header className="App-header">
        <div>
          <h1> BROCERIES </h1>
          <img src={logo}/>

           Split your groceries with your bros.

           <form action = "http://127.0.0.1:5000/uploadphoto" method = "POST"
              enctype = "multipart/form-data">
              <input type = "file" name = "file" />
              <input type = "submit"/>
           </form>
           </div>
        </header>
        <AddBro />
      </div>
    )
  }

}
export default App;
