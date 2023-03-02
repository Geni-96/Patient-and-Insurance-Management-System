import React from 'react';
import './recoveryLink.css';

export default function RecoveryLink(){
    return(
        <>
            <div class="card">
                <p class="lock-icon"><i class="fas fa-lock"></i></p>
                <h2>Password Reset</h2>
                <p>An email has been sent.</p><p> Please click the link in the email to reset your password.</p>
            </div>
        </>)
}
