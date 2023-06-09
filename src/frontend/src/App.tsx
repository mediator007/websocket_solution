import { Fragment, useState, useEffect, useRef, useMemo } from 'react';
import { Grid, GridItem } from '@consta/uikit/Grid';
import 'bootstrap/dist/css/bootstrap.min.css';
import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import Button from 'react-bootstrap/Button';

function App() {
  const [timerRun, setTimerRun] = useState<boolean>(false);
  const [timerValue, setTimerValue] = useState<string>();
  const [timerId, setTimerId] = useState<number>(0);

  const [websocket, setSocket] = useState<WebSocket>();

  const menu = useMemo(() => navBar(), [timerRun])
  
  function navBar () {
    return (
      <Navbar bg="bright" expand="lg">
        <Container>
          <Navbar.Brand href="#home"><b>Таймер</b></Navbar.Brand>
          <Navbar.Toggle aria-controls="basic-navbar-nav" />
          <Navbar.Collapse id="basic-navbar-nav">
            <Nav className="me-auto">
              {!timerRun && (
              <Button
                id='start_button'
                style={{marginLeft: "5%", width: "200px"}} 
                variant="success"
                onClick={()=>setTimerRun(true)}>
                  Старт</Button>
              )}
              {timerRun && (
              <Button
                id='start_button'
                style={{marginLeft: "5%", width: "200px"}}
                variant="danger"
                onClick={()=>setTimerRun(false)}>
                  Стоп</Button>
              )}
            </Nav>
          </Navbar.Collapse>
        </Container>
      </Navbar>
    );
  }
  
  function onMessage (ev: MessageEvent) {
    let recv = JSON.parse(ev.data)
    setTimerValue(recv.timer)
  };

  useEffect(()=> {
    if (timerRun){
      let ws = new WebSocket('ws://' + window.location.hostname + ':8000/api/ws');
      ws.onmessage = onMessage;
      setSocket(ws);
    } else {
      if (websocket) {
        websocket.close();
      };
    }
  }, [timerRun]);
  
  return (
    <Fragment>
      <>
      {menu}
      </>
      <Grid 
        cols="3" xAlign='center'
        style={{marginTop: "15%"}}>
        <GridItem col="1"/>
        <GridItem col="1">
          <div>Секунд с начала эпохи:</div>
          <div id='timer'><b>{timerValue}</b></div>
        </GridItem>
      </Grid>
    </Fragment>
  );
};

export default App;
