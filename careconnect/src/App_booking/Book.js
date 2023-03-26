import React from 'react'
import "./book.css"
import Calendar from 'react-calendar';

export default function Book(){
        const [datevalue, onChange] = React.useState(new Date());
        
        const [formData, setFormData] = React.useState(
            {
                time: "None", 
                reason:"",
            }
        )
        function handleChange(event) {
            console.log(event)
            setFormData(prevFormData => {
                return {
                    ...prevFormData,
                    [event.target.name]: event.target.value
                }
            })
        }
        function handleSubmit(event) {
            event.preventDefault()
            if(formData.time!== "None") {
                console.log("Successfully booked appointment")
            } else {
                console.log("Please select a time")
                return
            }
        }
      
    return(
        <div className="page">
            <nav className = "book-nav">
            <img src={process.env.PUBLIC_URL + "/react-logo.png"} className="logo"></img>
            <div className="search-wrap">
                <select class="dropdown">
                    <option value="Doctor">Doctor</option>
                    <option value="Insurance Provider">Insurance Provider</option>
                </select>
                <div className="search">
                    <input type="text" placeholder="Search"></input>
                    <button type="submit"><i class="fa fa-search"></i></button>
                    <button className="chat" type="text">CHAT</button>
                </div>
            </div>
        </nav>
        <div className="main">
            <div className='heading'><h2>Book Your Appointment</h2></div>
            <form className="contain" onSubmit={handleSubmit}> 
                <Calendar onChange={onChange} value={datevalue}  />
                <div className="time">
                    <p>Please select a time</p>
                    <select name="time" onChange={handleChange} id="time" value={formData.time}>
                        <option value="None">None</option>
                        <option value="10-11">10 a.m - 11 a.m</option>
                        <option value="11-12">11 a.m - 12 p.m</option>
                        <option value="4-5">4 p.m - 5 p.m</option>
                        <option value="5-6">5 p.m - 6 p.m</option>
                    </select>
                </div>
                <div className="reason">
                    <p>Please enter a reason for your visit: </p>
                    <textarea name="reason" onChange={handleChange} value={formData.reason} />
                </div>
                <button className="timesubmit">Submit</button>
            </form>
        
        </div>
        </div>
    )
}