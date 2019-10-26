import React from 'react';
import logo from './logo.svg';



class App extends React.Component {
  constructor () {
    super();
  }

  render() {
    return (
      <div className="App">
        <header className="App-header">
        <div>
          <h1> Broceries </h1>
           Split your groceries with your bros.

           <form action = "http://127.0.0.1:5000/uploadphoto" method = "POST"
              enctype = "multipart/form-data">
              <input type = "file" name = "file" />
              <input type = "submit"/>
           </form>
           </div>
        </header>
      </div>
    )
  }

}
export default App;
