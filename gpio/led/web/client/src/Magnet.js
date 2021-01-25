import React from 'react';
import Button from 'react-bootstrap/Button';

class Magnet extends React.Component {
  state = { isMagnetOn: false };

  handleClick = () => {
    const url = this.state.isMagnetOn ? '/leds/red/0' : 'leds/red/1';
    fetch(url, { method: 'PUT' })
      .then(response => response.status === 200 ?
              response.json() :
              Promise.reject("http error " + response.status))
      .then(result => this.setState({ isMagnetOn: result.active }))
      .catch(error => console.log("cannot reach server: " + error));
  }

  render() {
    return (
      <Button onClick={this.handleClick}>
        {this.state.isMagnetOn ? "magnets are on" : "magnets are off"}
      </Button>
    );
  }
}

export default Magnet;
