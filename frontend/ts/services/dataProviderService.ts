///<reference path="../models/frontendConfiguration.ts" />
///<reference path="../models/backendVersion.ts" />

type GPIOStateCallback = (gpioState: GPIOState) => void
type BackendVersionCallback = (backendVersion: BackendVersion) => void;
type GPIOConfigurationsCallback = (gpioConfiguration: GPIOConfiguration[]) => void;

class DataProviderService { 
    constructor(configuration: FrontendConfiguration) {
        console.log(configuration);
    }

    public fetchBackendVersion(callback: BackendVersionCallback): void {
        $.getJSON('/api/node/version', (data) => callback(<BackendVersion>data))
    }

    public fetchGPIOConfigurations(callback: GPIOConfigurationsCallback): void {
        $.getJSON('/api/node/gpioconfig', (data) => callback(<GPIOConfiguration[]>data))
    }

    public fetchGPIOState(gpio: number, callback: GPIOStateCallback): void {
        $.getJSON(`/api/node/get/${gpio}`, (data) => callback(<GPIOState>data));
    }
}