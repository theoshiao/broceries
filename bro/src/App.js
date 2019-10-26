import React from 'react';
import User from './User.js'
import AddUserForm from './AddUserForm.js'
// import ItemSelect from './ItemSelect.js'
import logo from './logo.svg';
import './App.css';
import {Col, Row, Jumbotron} from 'react-bootstrap';
// import '../node_modules/react-bootstrap'
// import Col from 'react-bootstrap/Col.js'
// import Row from 'react-bootstrap/Row.js'

class App extends React.Component {
  state = {
    users: [
    {
      name: "Me",
      items: [],
      id: 1
    }
  ]};

  handleAddUser = (name) => {
    this.setState( prevState => {
      return{
        users: [
          ...prevState.users,
          {
            name,
            items: [],
            id: this.prevPlayerId += 1
          }
        ]
    };
  });
  }

  handleRemoveUser = (id) => {
    this.setState( prevState => {
      return {
        users: prevState.users.filter(p => p.id !== id)
      };
    });
  }

  render() {
    return (
      <div className="App">
        <header className="App-header">
        <Row>
          <Col>
            <h1> BROCERIES </h1>
            <img src={logo}/>

             Split your groceries with your bros.

             <Col className="scoreboard">
             <h3 >Select Bros</h3>

               {this.state.users.map( (user, index) =>
                 <User className="player"
                     name={user.name}
                     items={user.items}
                     id={user.id}
                     index={index}
                     key={user.id.toString()}
                     removeUser={this.handleRemoveUser}
                     />

             )}
             <AddUserForm addUser={this.handleAddUser}/>
             <form action = "http://127.0.0.1:5000/uploadphoto" method = "POST"
                enctype = "multipart/form-data">
                <input type = "file" name = "file" />
                <input type = "submit"/>
             </form>
             </Col>

           </Col>
          </Row>
        </header>

      </div>
    )
  }

}
export default App;
