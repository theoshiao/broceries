import React from 'react';
import AddBro from './AddBro.js'


class App extends React.Component {
  state = {
    players: [
      {
        name: "Theo",
        id: 1
      },
      {
        name: "Anderson",
        id: 2
      },
      {
        name: "Nilay",
        id: 3
      },
      {
        name: "Amy",
        id: 4
      }
    ]
  };

  prevPlayerId = 4;


  handleAddPlayer = (name) => {
    this.setState( prevState => {
      return{
        players: [
          ...prevState.players,
          {
            name,
            id: this.prevPlayerId += 1
          }
        ]
    };
  });
  }

  handleRemovePlayer = (id) => {
    this.setState( prevState => {
      return {
        players: prevState.players.filter(p => p.id !== id)
      };
    });
  }

  render() {
    return (
      <div className="scoreboard">
        {/* Players list */}
        {this.state.players.map( (player, index) =>
          <Player
            name={player.name}
            id={player.id}
            index={index}
            changeScore={this.handleScoreChange}
            key={player.id.toString()}
            removePlayer={this.handleRemovePlayer}
          />
        )}
        <AddBro addPlayer={this.handleAddPlayer}/>
      </div>
    );
  }
}

export default App;
