import React from 'react';
import Button from 'react-bootstrap/Button';

class VacuumPump extends React.Component {
  state = { isVacuumOn: false };

  handleClick = () => {
    const url = this.state.isVacuumOn ? '/leds/green/0' : 'leds/green/1';
    fetch(url, { method: 'PUT' })
      .then(response => response.json())
      .then(result => this.setState({ isVacuumOn: result.active }));
  }

  render() {
    return (
      <Button onClick={this.handleClick}>
        {this.state.isVacuumOn ? "vacuum pump is on" : "vacuum pump is off"}
      </Button>
    );
  }
}

export default VacuumPump;
