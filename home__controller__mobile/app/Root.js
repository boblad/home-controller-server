import React, { Component } from 'react';
import {
  View,
  TouchableOpacity,
  StyleSheet,
  Text
} from 'react-native';

class Root extends Component {
  render() {
    return (
      <View style={styles.container} >
        <TouchableOpacity style={styles.button} onPress={this.handlePress.bind(this)}>
          <Text>Toggle</Text>
        </TouchableOpacity>
      </View>
    );
  }

  handlePress() {

    fetch('http://b210b49d.ngrok.io/lights/on')
    .then(res => {})

  }
}

const styles = StyleSheet.create({
  button: {
    width: 100,
    height: 50,
    backgroundColor: 'grey',
    justifyContent: 'center',
    alignItems: 'center'
  },
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  }
})

export default Root;
