import React from 'react';
import './reset.css';
import CareConnect from '../LoginPage/CareConnect.png'

export default function Reset(){
    return(
        <>
            <div className="card">
            <img className="logo" src={CareConnect} alt="logo"></img>
                <div className="innerCard">
                    <p className="lock-icon"><i className="fas fa-lock"></i></p>
                    <h2>Change Password</h2>
                    <p>To protect your account, create a password that:</p>
                    <ul>
                        <li>Has at least 10 characters</li>
                        <li className="list">Contains at least 1 uppercase letter, 1 lowercase letter, 1 number, and 1 special character</li>
                        <li>Does not contain any part of your name</li>
                        <li>Is not one of your previously used passwords</li>
                    </ul>
                    <p className="passwd">New Password</p>
                    <input type="password" className="passInput"></input>
                    <p className="passwd">Re-enter Your New Password</p>
                    <input type="password" className="passInput"></input>
                    <button>Change My Password</button>
                </div>
            </div>
        </>)
}
