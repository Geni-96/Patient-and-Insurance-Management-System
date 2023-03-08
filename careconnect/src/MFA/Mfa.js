import "./mfa.css"
import React from 'react'

export default function Mfa(){
    return(<div className="mfapage">
            <div className="container">
                <div className = "row">
                    <div className = "col">
                        <img src={require("./react-logo.png")} />
                        <h2>Two Factor Authentication</h2>
                        <p>Please enter the Two-step verification code you have received on your email.</p>
                        <div class="input-group flex-nowrap">
                        <input type="text" class="form-control" placeholder="Enter your unique code" />
                        </div>
                        <button type="button" class="btn btn-success col-6">Verify</button><br/>
                        <a className="mb-5 pb-lg-2" href="/login">Go back</a>
                    </div>
                </div>
            </div>
    </div>
    )
}