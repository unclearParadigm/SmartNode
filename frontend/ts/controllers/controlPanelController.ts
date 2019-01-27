///<reference path="../services/dataProviderService.ts" />

class ControlPanelController {
    private readonly headerbar: Headerbar;
    private digitalSwitches: DigitalSwitch[];

    private readonly siteLayout: string = `
        <div class="container">
            <section class="section js-header"></section>
            <section class="columns is-8 is-centered is-vcentered js-controls"></section>
        </div>
    `;

    constructor(
        private readonly container: JQuery, 
        private readonly dataService: DataProviderService) {

        this.container.html(this.siteLayout);
        this.headerbar = new Headerbar();
        this.digitalSwitches = [];
    }
    
    public display() {
        this.dataService.fetchBackendVersion((backendVersion) => {
            this.headerbar.setBackendVersion(backendVersion.version);
            this.container.find('.js-header').html(this.headerbar.render());
        });

        this.dataService.fetchGPIOConfigurations((gpioConfigurations) => {
            gpioConfigurations.forEach(config => {
                const controlContainerClass = `js-control-wrapper-${config.gpio}`;
                this.container
                    .find('.js-controls')
                    .append(`<div class="${controlContainerClass}"></div>`);
                const controlContainer = this.container.find(`.${controlContainerClass}`);
                this.digitalSwitches.push(new DigitalSwitch(controlContainer, this.dataService, config, 1000));
                this.digitalSwitches.forEach(x => x.start());
            });
        });
    }
}
