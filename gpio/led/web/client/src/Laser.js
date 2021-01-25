import React from 'react';
import Button from 'react-bootstrap/Button';

class Laser extends React.Component {
  state = {
    isLaserOn: false,
  };

  laserButtonClicked = () => {
    const url = this.state.isLaserOn ? '/leds/blue/0' : 'leds/blue/1';
    fetch(url, { method: 'PUT' })
      .then(response => response.json())
      .then(result => this.setState({ isLaserOn: result.active }));
  }

  render() {
    return (
      <Button onClick={this.laserButtonClicked}>
        {this.state.isLaserOn ? "laser is on" : "laser is off"}
      </Button>
    );
  }
}

export default Laser;
