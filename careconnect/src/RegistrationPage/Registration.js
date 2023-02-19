import "./registration.css"


export default function Registration(){
    return(
    <div className="regpage">
        <div className="cover">
            <h2>Registration</h2>
            <form action="form.html"/>
            <div id="usertype">
              <label className="usertype">Doctor</label>
              <input type="radio" id="doctor" value="Doctor" name="usertype"/>
              <label className="usertype">Patient</label>
              <input type="radio" id="patient" value="Patient" name="usertype"/>
              <label className="usertype">InsuranceProvider</label>
              <input type="radio" id="insuranceprovider" value="Insurance Provider" name="usertype"/><br/>
            </div>
            <div className="inputboxes">
            <div className="input1">
            <label>First Name</label>
            <input type="text" placeholder="Enter your first name" id="box" required/><br/>
            <label>Last Name</label>
            <input type="text" placeholder="Enter your last name" id="box" required/><br/>
            <label>Email</label>
            <input type="text" placeholder="Enter your email" id="box" required/><br/>
            </div>
            <div className="input2">
            <label>Password</label>
            <input type="password" placeholder="Enter your password" id="box" required/><br/>
            <label>Re-type Password</label>
            <input type="password" placeholder="Confirm your password" id="box" required/><br/>
            <label>Phone number</label>
            <input type="numeric" placeholder="Enter your phone number" id="box" required/><br/>
            </div>
            </div>
            <div id="gender">
            <label>Gender</label><br/>
              <label name="gender">Male</label>
              <input type="radio" id="male" value="Male" name="gender"/>
              <label name="gender">Female</label>
              <input type="radio" id="female" value="Female" name="gender"/>
              <label name="other">Other</label>
              <input type="radio" id="other" value="Other" name="gender"/><br/>
            </div>
            <input type="submit" id="submit" value="Submit"></input>
        </div>
    </div>)
}