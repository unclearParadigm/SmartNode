///<reference path="./controllers/devAdController.ts" />
///<reference path="./controllers/controlPanelController.ts" />

///<reference path="./models/frontendConfiguration.ts" />
///<reference path="./services/dataProviderService.ts" />

function Initialize(config: FrontendConfiguration): void {
    if(config === null || config === undefined) 
        console.error('Whoops, You forgot to pass the Configuration, silly :/');
    
    let devAdController = new DevAdController();
    devAdController.display();

    let dataProvider = new DataProviderService(config);
    let controlPanel = new ControlPanelController($('body'), dataProvider);
    controlPanel.display();
};
