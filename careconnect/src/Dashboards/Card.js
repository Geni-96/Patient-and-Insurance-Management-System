import React from "react"
import "./dashboard_styles.css"
// import Card from 'react-bootstrap/Card';
// import Button from 'react-bootstrap/Button';

export default function Cards(props) {
    // const [appointment,setAppointment] = React.useState({
    //     doctorName: "",
    //     date: "",
    //     time: ""
    // })
    // const [app,setApp] = React.useState([])

    // React.useEffect(() => {
    //     fetch("#")
    //     .then(res => res.json())
    //     .then(data => setApp(data))
    // })
    return (
        // <Card className="mx-auto" style={{ width: '68rem' }}> 
        // <Card.Body >
        //     <div className="Details">
        //         <Card.Title>{props.doctorName}</Card.Title>
        //         <p>Date: {props.date}</p>
        //         <p>Time: {props.time}</p>
        //     </div>
        //     <div className="buttons">
        //         <Button className="doc-buttons" variant="primary">View Patient's Profile</Button>
        //         <Button className="doc-buttons" variant="primary">SEND A TEXT</Button>
        //         <Button className="doc-buttons" variant="primary">Cancel Appointment</Button>
        //     </div>
        // </Card.Body>
        // </Card>
        <div className="section">
            <div className="container">
                <div className="Details">
                    <h2>{props.doctorName}</h2>
                    <p>Date: {props.date}</p>
                    <p>Time: {props.time}</p>
                </div>
                <div className="buttons">
                    <button className="doc-buttons">View Patient's Profile</button>
                    <button className="doc-buttons">SEND A TEXT</button>
                    <button className="doc-buttons">Cancel Appointment</button>
                </div>
            </div>
        </div>
    )
}