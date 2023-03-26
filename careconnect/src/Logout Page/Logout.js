import React from 'react';
import './logout.css';
import CareConnect from '../LoginPage/CareConnect.png'
import hands from './hands.jpg'

export default function Logout(){
    return(
        <>
            <div className="container">
                <div className="column1">
                <img className="logo" src={CareConnect} alt="logo"></img>
                    <h1>You have been successfully logged out.</h1>
                    <p>Thank you for using CareConnect for all of your healtcare needs.</p>
                    <button>Sign in again</button>
                </div>
                <div className="column2">
                    <img className="hands" src={hands} alt="logo"></img>
                </div>
            </div>
        </>)
}
