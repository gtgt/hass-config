#include "esphome.h"
#include "esphome/components/thermostat/thermostat_climate.h"

class RoomThermostatClimate : public thermostat::ThermostatClimate {
 public:
  void setup() override {
    ThermostatClimate::setup();
    this->set_supports_two_points(false);
  }
  ClimateTraits traits() override {
    // The capabilities of the climate device
    auto traits = ThermostatClimate::traits();

    return traits;
  }
};
