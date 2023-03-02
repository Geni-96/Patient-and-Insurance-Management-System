import React from 'react';
import './pwd.css';

export default function Pwd(){
    return(
        <>
            <div class="card">
                <p class="lock-icon"><i class="fas fa-lock"></i></p>
                <h2>Forgot Password?</h2>
                <p>You can reset your Password here.</p>
                <input type="text" class="passInput" placeholder="Enter your email address"></input>
                <button>Send My Password</button>
            </div>
        </>)
}
