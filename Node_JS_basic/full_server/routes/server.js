import express from 'express';
import controllerRouting from './index';

const app = express();
const port = 1245;

controllerRouting(app);

app.listen(port, () => {

});

export default app;
