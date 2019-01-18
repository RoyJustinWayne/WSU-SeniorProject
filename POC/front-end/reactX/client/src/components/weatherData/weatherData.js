import React, { Component } from 'react';
import ReactTable from "react-table";
import './weatherData.css';


class WeatherData extends Component {
    constructor() {
        super();
        this.state = {
            weather: []
        }
    }

    fetchResult = () => {
        fetch('/api/weatherData')
                .then(res => res.json())
                .then(weather => this.setState({weather}, () => console.log('Weather fetched...', weather)));
    }

    componentDidMount() {
        this.fetchResult()
        setInterval(this.fetchResult, 10000)
    }

    

    render() {
        return (
        <div class="customTable">
            <ul>
                <li class="table-header">
                    <div class="col col-1">Time</div>
                    <div class="col col-2">apiKey</div>
                    <div class="col col-3">Temperature</div>
                    <div class="col col-4">Humidity</div>
                    <div class="col col-5">Pressure</div>
                    <div class="col col-6">Latitude</div>
                    <div class="col col-7">Longitude</div>
                </li>
                {this.state.weather.map(weather => <li class="table-row" key={weather.id}>
                    <div class="col col-1">{weather.time}</div>
                    <div class="col col-2">{weather.apiKey}</div>
                    <div class="col col-3">{weather.temp}</div>
                    <div class="col col-4">{weather.humidity}</div>
                    <div class="col col-5">{weather.pressure}</div>
                    <div class="col col-6">{weather.latitude}</div>
                    <div class="col col-7">{weather.longitude}</div>
                    </li>)
                }
            </ul>
        </div>
        );
  }
}

export default WeatherData;
